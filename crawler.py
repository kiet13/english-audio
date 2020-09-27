from bs4 import BeautifulSoup
import requests


def crawl_word_audio_url(word, url='https://www.ldoceonline.com/'):
    req = requests.get(url + '/dictionary/' + word)
    soup = BeautifulSoup(req.text, "html.parser")
    spans = soup.find_all('span', attrs={'class':'speaker amefile fas fa-volume-up hideOnAmp'})
    
    audio_url = None
    if len(spans) > 0:
        audio_url = spans[0]['data-src-mp3']

    return audio_url

def download_audio(audio_url):
    audio = requests.get(audio_url)
    with open('movie.mp3', 'wb') as f:
        f.write(audio.content)