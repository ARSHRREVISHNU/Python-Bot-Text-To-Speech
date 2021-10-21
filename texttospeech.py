from gtts import gTTS
import os
import PyPDF2
#open pdf
book = open('sampledoc.pdf', 'rb')
pdfreader = PyPDF2.PdfFileReader(book)
page = pdfreader.getPage(0)
#extractig the text
text = page.extractText()
mytext = text
language = 'en'
myfile = gTTS(text=mytext, lang=language, slow=False)
filename = input("Enter a file name for your audio file:")
myfile.save(filename+".mp3")

os.system(filename+".mp3")
