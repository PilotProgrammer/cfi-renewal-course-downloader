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
    '1317': range(1, 50),
    '1318': range(1, 50),
    '1319': range(1, 50),
    '1320': range(1, 50),
    '1321': range(1, 50),
    '1322': range(1, 50)
}

headers = {"Cookie": "ASP.NET_SessionId=<<CRED>>; Username=<<CRED>>; ASPSESSIONIDSCVTDSRQ=<<CRED>>;"}

chapterNames = list(chapters.keys())

def combinePdfs(chapterPdfFileNames, chapterName):
	pdfWriter = PyPDF2.PdfFileWriter()

	for filename in chapterPdfFileNames:
		pdfFileObj = open(filename, 'rb')
		pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

		for pageNum in range(pdfReader.numPages):
			pageObj = pdfReader.getPage(pageNum)
			pdfWriter.addPage(pageObj)

	pdfOutput = open(chapterName + '.pdf', 'wb')
	pdfWriter.write(pdfOutput)
	pdfOutput.close()

def sanitizeForm(theForm):
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

	return theForm

def isLastPageOfChapter(theForm):
	hasSection = False
	for element in theForm.find_all('div', {'class': 'Section'}):
		if element is not None:
			hasSection = True
			break

	return not hasSection


for chapterName in chapterNames:
	pageNums = chapters[chapterName]
	chapterPdfFileNames = []

	for pageNum in pageNums:
		print(f'Chapter {chapterName} page number {pageNum}')
		URL = f"https://americanflyers.net/content/browser/chapter.aspx?CID={chapterName}&Page={pageNum}"

		resp = requests.get(url=URL, headers=headers)  # , params = PARAMS)
		soup = BeautifulSoup(resp.text, features="html.parser")
		theForm = soup.find(id='aspnetForm')

		theForm = sanitizeForm(theForm)

		if isLastPageOfChapter(theForm) == True:
			print (f'No Section, must be last page of chapter...')
			break
		
		htmlFileName = f'firc-{chapterName}-{pageNum}.html'
		chapterPdfFileName = f'firc-{chapterName}-{pageNum}.pdf'
		chapterPdfFileNames.append(chapterPdfFileName)

		with open(htmlFileName, 'w') as file:  # Use file to refer to the file object
				file.write(str(theForm))

		pdfkit.from_file(htmlFileName, chapterPdfFileName)
		os.remove(htmlFileName)

	combinePdfs(chapterPdfFileNames, chapterName)

	for chapterPdfFileName in chapterPdfFileNames:
		os.remove(chapterPdfFileName)
