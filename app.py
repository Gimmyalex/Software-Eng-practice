# ...

from flask import Flask, render_template, request, send_file
from gtts import gTTS
import PyPDF2
import io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return render_template('index.html', error='No file part')

        file = request.files['file']

        # Check if the file is empty
        if file.filename == '':
            return render_template('index.html', error='No selected file')

        # Check if the file is a PDF
        if file and file.filename.endswith('.pdf'):
            pdfreader = PyPDF2.PdfReader(file)
            combined_text = ""

            # Iterate through pages
            for page_num in range(len(pdfreader.pages)):
                text = pdfreader.pages[page_num].extract_text()
                clean_text = text.strip().replace('\n', ' ')
                combined_text += clean_text + " "

            # Generate audio
            speaker = gTTS(text=combined_text, lang='en', slow=False)
            audio_file = io.BytesIO()
            speaker.write_to_fp(audio_file)
            audio_file.seek(0)

            # Return the audio file for download
            return send_file(io.BytesIO(audio_file.read()),
                             mimetype='audio/mpeg',
                             as_attachment=True,
                             download_name='output.mp3')

        else:
            return render_template('index.html', error='Invalid file format. Please upload a PDF file.')

    return render_template('index.html', error=None)

if __name__ == '__main__':
    app.run(debug=True)
