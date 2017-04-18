import bs4
import csv
import os
import sys

def main():
    output_dir = os.path.abspath(sys.argv[1])
    os.chdir(sys.path[0])
    with open('canonicals.csv', 'r') as csv_f:
        reader = csv.reader(csv_f)
        for row in reader:
            source_file, canonical_url = row
            with open(os.path.join(
                    output_dir, source_file.replace('.dita', '.html')
                    ), 'r+') as html_f:
                soup = bs4.BeautifulSoup(html_f.read(), 'html.parser')
                link = soup.new_tag('meta')
                link.attrs['name'] = 'canonical_url'
                link.attrs['content'] = canonical_url
                soup.head.insert(0, link)
                html_f.seek(0)
                html_f.write(soup.prettify())


if __name__ == '__main__':
    main()
