from bs4 import BeautifulSoup
import requests



def crawl_word_audio_url(word, url='https://www.dictionary.com'):
    req = requests.get(url + '/browse/' + word)
    soup = BeautifulSoup(req.text, "html.parser")
    audio_tag = soup.find('audio')
    audio_url = audio_tag.find("source", {"type":"audio/mpeg"}).get("src")
    return audio_url

if __name__ == "__main__":
    audio_url = crawl_word_audio_url("apple")
    print(audio_url)
