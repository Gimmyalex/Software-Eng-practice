import pyttsx3,PyPDF2

from PyPDF2 import PdfReader

#insert name of your pdf 
pdfreader = PyPDF2.PdfReader(open('Babypips Forex - School of Pipsology_Part 1-3.pdf', 'rb'))
speaker = pyttsx3.init()

for page_num in range(len(pdfreader.pages)):
    text = pdfreader.pages(page_num).extractText()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)
#name mp3 file whatever you would like
speaker.save_to_file(clean_text, 'story.mp3')
speaker.runAndWait()

speaker.stop()