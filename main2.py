import PyPDF2
from gtts import gTTS

# Insert the name of your PDF
pdf_path = 'Babypips Forex - School of Pipsology_Part 1-3.pdf'

pdfreader = PyPDF2.PdfReader(open(pdf_path, 'rb'))

# Initialize an empty string to store the combined text
combined_text = ""

# Iterate through pages using the correct indexing
for page_num in range(len(pdfreader.pages)):
    text = pdfreader.pages[page_num].extract_text()
    clean_text = text.strip().replace('\n', ' ')
    combined_text += clean_text + " "
    print(clean_text)

# Create gTTS object with combined text
speaker = gTTS(text=combined_text, lang='en', slow=False)

# Save the speech as an MP3 file
speaker.save('story.mp3')

# Run the text-to-speech engine
speaker.runAndWait()
