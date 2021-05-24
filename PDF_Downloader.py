import requests
from bs4 import BeautifulSoup as BS
import os


def pdf_downloader(url=''):
    downloaded_files = 0
    skipped_files = 0
    pdfs = []

    current_directory = os.path.curdir

    export_path = os.path.join(current_directory, 'downloads')
    if not os.path.exists(export_path):
        os.mkdir(export_path)

    # if no URL given, ask for one
    if url == '':
        url = str(input('Input target URL: '))
    r = requests.get(url)

    if r.status_code == 200:
        soup = BS(r.content, features='html.parser')
        links = soup.find_all('a')

        for link in links:
            if 'href' in link.attrs:
                if link.attrs['href'].endswith('.pdf'):
                    pdfs.append(link.attrs['href'])

        print(f'Total PDFs found: {len(pdfs)}')

        for url in pdfs:
            filename = os.path.basename(url)
            download_path = os.path.join(export_path, filename)

            if not os.path.exists(download_path):
                with open(download_path, 'wb') as pdf:
                    r = requests.get(url)
                    pdf.write(r.content)
                print(f'Downloaded file: {filename}')
                downloaded_files += 1

            else:
                print(f'File already downloaded: {filename}')
                skipped_files += 1

        print(f'''
DOWNLOAD COMPLETE
  PDFs Downloaded: {downloaded_files} 
  PDFs Skipped:    {skipped_files}
  Total files:     {downloaded_files + skipped_files}''')
    else:
        print(f'ERROR {r.status_code}: unable to connect')


if __name__ == '__main__':
    pdf_downloader()
