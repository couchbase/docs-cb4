import bs4
import csv
import os
import sys

def main():
    output_dir = os.abspath(sys.argv[1])
    os.chdir(sys.path[0])
    with open('canonicals.csv', 'r') as csv_f:
        reader = csv.reader(csv_f)
        for row in reader:
            source_file, canonical_url = row
            with open(os.path.join([
                    output_dir, source_file.replace('.dita', '.html')
                    ])) as html_f: 
                soup = bs4.BeautifulSoup(html_f.read(), 'html.parser')
                link = soup.new_tag('link')
                link.attrs['rel'] = 'canonical'
                link.attrs['href'] = canonical_url
                soup.head.insert(0, link)

if __name__ == '__main__':
    main()
