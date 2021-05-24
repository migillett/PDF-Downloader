# PDF-Downloader
This simple program uses the BeautifulSoup and requests libraries to get a list of all PDFs from a specific URL and downloads them for archiving.

## How to Use
Simply start the program using the command `python3 PDF_Downloader.py`. It will then ask you to input a target URL to pull from. You can also do this directly from the PDF_Downloader.py file if you pass it in as the `url=''` argument for the function, `pdf_downloader()`.

## Requirements
This program requires BeautifulSoup4 and requests. To install, run the command `pip3 install requests beautifulsoup4` or use the `requirements.txt` file.
