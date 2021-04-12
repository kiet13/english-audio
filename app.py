from flask import Flask, render_template, request, jsonify
import crawler

app = Flask(__name__, template_folder='templates')

# a simple home page with textbox to input English word
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/audio', methods=['GET'])
def get_audio():
    if request.method == 'GET':
        english_word = request.args.get('word')
        audio_url = crawler.crawl_word_audio_url(english_word)
        
        return render_template('home.html', word=english_word, audio=audio_url)

if __name__ == '__main__':
    app.run(debug=True, port='3000')
