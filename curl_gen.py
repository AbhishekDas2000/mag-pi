import requests as req
from urllib import request
from bs4 import BeautifulSoup
from tqdm import tqdm

BASE_URL = "https://magpi.raspberrypi.com"
ISSUES = "/issues/"
TAIL = "/pdf/download"
FILE_NAME_HEADER = "Magpi"
FILE_EXTENSION = ".pdf"
ISSUE_START = 115
ISSUE_END = 122


for pdf_number in tqdm(range(ISSUE_START, ISSUE_END + 1)):

    url= BASE_URL + ISSUES + str(pdf_number) + TAIL
    file = FILE_NAME_HEADER + str(pdf_number) + FILE_EXTENSION

    page = req.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    result = soup.find("iframe", class_ = "u-hidden")

    download_url = BASE_URL + str(result['src'])

    # TODO request.urlretrieve() may get deprecated in the future.
    request.urlretrieve(download_url, file)

