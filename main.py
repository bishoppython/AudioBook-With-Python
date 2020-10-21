#Biblioteca Necessária para windows - pywin32
#Disponível em https://github.com/mhammond/pywin32/releases/tag/b221
#https://pypi.org/simple/pypiwin32/

import pyttsx3
import PyPDF2
arquivo = open('arquivo.pdf', 'rb') #Faz a leitura binaria do arquivo em PDF
pdfReader = PyPDF2.PdfFileReader(arquivo) # Faz a leitura do arquivo
pages = pdfReader.numPages # Gera numero de paginas

speaker = pyttsx3.init() #inicia a biblioteca de speaker(fala)

#Para num leia pages, ou seja, caso deseje ler de um determinada pagina acrescentar a numeração exemplo (5,pages)
for num in range(pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
