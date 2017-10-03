from __future__ import print_function
import xml.etree.ElementTree as etree
import re
import os
import logging
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger('TransformMan')


def convert_file(path):
    substitute_regex = re.compile('\(\d*\)')
    tree = etree.parse(path)
    root = tree.getroot()
    root_topic = root.find('.//topic')
    title = root.find('.//topic/title')
    title.text = substitute_regex.sub('', title.text).replace('couchbase-cli-', '')
    to_remove = [root.find('.//topic/topic[@id="_see_also"]'),
                 root.find('.//topic/topic[@id="_couchbase_cli"]')]

    name_topic = root.find('.//topic/topic[@id="_name"]')
    name_topic_content = root.find('.//topic/topic[@id="_name"]/body/p')
    short_desc = name_topic_content.text.split(' - ', 1)[1]
    root_topic.remove(name_topic)
    
    synopsis_topic = root.find('.//topic/topic[@id="_synopsis"]/body')
    synopsis_lq = root.find('.//topic/topic[@id="_synopsis"]/body/lq')
    synopsis_lines = root.find('.//topic/topic[@id="_synopsis"]/body/lq/lines/*')
    
    synopsis_content = etree.tostring(synopsis_lines, encoding="unicode").replace('\n', '')
    synopsis_content = ' '.join(synopsis_content.split())

    syntax_codeblock = etree.XML('<codeblock outputclass="language-bash">{}</codeblock>'.format(synopsis_content))
    synopsis_topic.remove(synopsis_lq)
    synopsis_topic.append(syntax_codeblock)
    synopsis_title = root.find('.//topic/topic[@id="_synopsis"]/title')
    synopsis_title.text = 'SYNTAX'

    links = root.findall('.//topic/topic[@id="_see_also"]/body/p/cite//ph')
    links_to_create = []
    for child in links:
        try:
            int(child.text)
        except ValueError:
            href = substitute_regex.sub('', child.text)

            if href == 'couchbase-cli':
                continue

            if not href.startswith('couchbase-cli-'):
                href = href.replace('couchbase', 'couchbase-cli')
            links_to_create.append(href)
    
    for element in to_remove:
        root_topic.remove(element)
    
    for topic in root_topic.findall('./topic'):
        topic_body = topic.find('./body')
        section = etree.Element('section')
        section.append(topic.find('./title'))
        section.extend(topic_body)
        root_topic.remove(topic)
        root_topic.find('./body').append(section)

    root_topic.remove(root_topic.find('./prolog'))
    related_links = etree.Element('related-links')

    for link in links_to_create:
        link_element = etree.XML('<link href="{}.dita"/>'.format(link))
        related_links.append(link_element)
    
    short_desc = etree.XML('<shortdesc>{}</shortdesc>'.format(short_desc))
    root_topic.insert(1, short_desc)
    root_topic.append(related_links)
    
    result = '<?xml version="1.0" standalone="no"?>'
    result += '<!DOCTYPE dita PUBLIC "-//OASIS//DTD DITA Composite//EN" "../../../../dtd/ditabase.dtd">'
    result += etree.tostring(root, encoding="unicode")
    return result

def main():
    for filename in os.listdir('.'):
        if filename.startswith('couchbase-cli-'):
            try:
                content = convert_file(filename)
            except Exception:
                LOGGER.exception('File {} failed'.format(filename))
            else:
                with open(filename, 'w') as f:
                    f.write(content)
                LOGGER.info('File {} transformed'.format(filename))
        
if __name__ == "__main__":
    main()