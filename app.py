from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
import crawler
import os
import re
import requests
from datetime import date
from werkzeug.utils import secure_filename

today = date.today()
month = str(today.month).rjust(2, '0')
year = str(today.year)

ALLOWED_EXTENSIONS = {'txt', 'pdf'}
SAVE_FOLDER = f'D:/Vocabulary/{month}-{year}'

app = Flask(__name__, template_folder='templates')
app.config['SAVE_FOLDER'] = SAVE_FOLDER

# a simple home page with textbox to input English word
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/audio', methods=['POST'])
def get_audio():
    if request.method == 'POST':
        english_word = request.form['search']
        if english_word:
            audio_url = crawler.crawl_word_audio_url(english_word)
            return render_template('home.html', word=english_word, audio=audio_url)

        
        # check if request has the file part
        app.logger.info(request.files)
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)

            if not os.path.isdir(app.config['SAVE_FOLDER']):
                os.mkdir(app.config['SAVE_FOLDER'])

            path = os.path.join(app.config['SAVE_FOLDER'], filename)
            app.logger.info('Save file as: %s', path)
            file.save(path)
            app.logger.info('Upload file successfully!')
            with open(path) as f:
                data = [line for line in f.read().splitlines() if len(line) > 0]
                app.logger.info(data)
            
            count = 0
            for line in data:
                word = re.search(r'[a-zA-Z-]+', line).group()
                app.logger.info('%s', word)
                audio_url = crawler.crawl_word_audio_url(word)
                if len(audio_url) > 0:
                    r = requests.get(audio_url, allow_redirects=True)
                    open(f'{SAVE_FOLDER}/{word}.mp3', 'wb').write(r.content)
                    count += 1
            
            return render_template('home.html', num_words=count)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run(port='2000', debug=True)
