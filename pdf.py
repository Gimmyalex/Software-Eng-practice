import PyPDF2
from gtts import gTTS
import io

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

# Split the combined text into chunks of 500 characters (you can adjust this value)
text_chunks = [combined_text[i:i+500] for i in range(0, len(combined_text), 500)]

# Initialize an empty string to store the final combined audio
combined_audio = ""

# Generate audio for each chunk
for chunk in text_chunks:
    speaker = gTTS(text=chunk, lang='en', slow=False)
    audio_chunk = speaker.get_audio_data()
    combined_audio += audio_chunk

# Save the combined audio as an MP3 file
with open('story.mp3', 'wb') as audio_file:
    audio_file.write(combined_audio)
