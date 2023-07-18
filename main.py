#Pdf Reader

import pyttsx3
import PyPDF2
book = open('oop.pdf', 'rb')
pdf_Reader = PyPDF2.PdfFileReader(book)
pages = pdf_Reader.numPages

speaker = pyttsx3.init()
for num in range(7, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
