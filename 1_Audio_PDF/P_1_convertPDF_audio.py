import pyttsx3, PyPDF2

#Get the pdf
pdfreader = PyPDF2.PdfReader(open('book.pdf', 'rb'))
speaker =  pyttsx3.init()

#reading the pages
for pageNum in range(len(pdfreader.pages)):
    text = pdfreader.pages[pageNum]
    cleanText = text.extract_text()
    print(cleanText)

#saving the file
speaker.save_to_file(cleanText, 'story.mp3')
speaker.runAndWait()

#ending the convertions
speaker.stop()