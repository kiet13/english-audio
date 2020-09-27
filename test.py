from bs4 import BeautifulSoup
import requests
url = "https://www.ldoceonline.com/"
word = 'apple'
req = requests.get(url + '/dictionary/' + word)
soup = BeautifulSoup(req.text, "html.parser")

spans = soup.find_all('span', attrs={'class':'speaker amefile fas fa-volume-up hideOnAmp'})
audio_url = spans[0]['data-src-mp3']


