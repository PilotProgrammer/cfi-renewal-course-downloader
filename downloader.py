import requests
import pdfkit
import os
from bs4 import BeautifulSoup
import PyPDF2

# TODO
# 1. make this a library
# 2. multi-threaded
# 3. get list of chapters automatically?

chapters = {
    '1317': range(1, 20)
}

headers = {"Cookie": "<<your creds here>>"}


chapterNames = list(chapters.keys())

htmlFileNames = []
chapterPdfFileNames = []


def combinePdfs(chapterPdfFileNames):
	pdfWriter = PyPDF2.PdfFileWriter()

	for filename in chapterPdfFileNames:
		pdfFileObj = open(filename, 'rb')
		pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

		for pageNum in range(pdfReader.numPages):
			pageObj = pdfReader.getPage(pageNum)
			pdfWriter.addPage(pageObj)

	pdfOutput = open('out.pdf', 'wb')
	pdfWriter.write(pdfOutput)
	pdfOutput.close()


for chapterName in chapterNames:
	pageNums = chapters[chapterName]

	for pageNum in pageNums:
		print(f'pageNum {pageNum}')
		URL = f"https://americanflyers.net/content/browser/chapter.aspx?CID={chapterName}&Page={pageNum}"
		htmlFileName = f'firc-{chapterName}-{pageNum}.html'
		chapterPdfFileName = f'firc-{chapterName}-{pageNum}.pdf'
		htmlFileNames.append(htmlFileName)
		chapterPdfFileNames.append(chapterPdfFileName)

		resp = requests.get(url=URL, headers=headers)  # , params = PARAMS)
		soup = BeautifulSoup(resp.text, features="html.parser")
		theForm = soup.find(id='aspnetForm')

		# remove executable code and links to content which may not be reachable from script (just keep content text and images)
		for element in theForm.find_all('script'):
				element.decompose()

		for element in theForm.find_all('style'):
				element.decompose()

		for element in theForm.find_all('a'):
				element.decompose()

		for element in theForm.find_all('iframe'):
				element.decompose()

		# remove navigation divs, with dead links to navigation icons
		for element in theForm.find_all('div', {'class': 'NavControl'}):
				element.decompose()

		hasSection = False
		for element in theForm.find_all('div', {'class': 'Section'}):
			if element is not None:
				hasSection = True
				break

		if hasSection == False:
			print (f'No Section, must be last page, ending...')
			break

		with open(htmlFileName, 'w') as file:  # Use file to refer to the file object
				file.write(str(theForm))

		pdfkit.from_file(htmlFileName, chapterPdfFileName)
		os.remove(htmlFileName)

		# if pageNum > 3:
		# 	break

	combinePdfs(chapterPdfFileNames)

	for chapterPdfFileName in chapterPdfFileNames:
		os.remove(chapterPdfFileName)
