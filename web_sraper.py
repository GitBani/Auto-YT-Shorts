from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
from gtts import gTTS
from openai import OpenAI
from pydub import AudioSegment


url = "https://www.reddit.com/r/AmItheAsshole/top?limit=10/"#'https://www.reddit.com/r/UnethicalLifeProTips/top/'#'https://www.reddit.com/r/TalesFromRetail/top/'#
output_file = 'speech.mp3'



headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
response = requests.get(url, headers = headers) 
html = response.text


soup = BeautifulSoup(html, "html.parser")


def post_selector(tag):
    return tag.name == 'shreddit-post'  


# body is 4 if there is a flair, else its 3
posts = soup.find_all(post_selector)
print(len(posts))
link_with_post_title = posts[0].find_all('a')[0]
link_with_post_body = posts[0].find_all('a')[4]

title = link_with_post_title.attrs.get('aria-label')


body = ""
for paragraph in link_with_post_body.find_all('p'):
    body += paragraph.getText()


text = title + body
text = text.replace('AITA', 'Am I the A-hole')
text = text.replace('ULPT', 'Unethical life pro tip')
text = text.replace('\n', '')
print(len(text))
exit(0)

load_dotenv()
client = OpenAI()
response = client.audio.speech.create(
    model = 'tts-1',
    voice = 'onyx',
    input = text
)
response.stream_to_file(output_file)

audio = AudioSegment.from_file(output_file, format="mp3")
faster_audio = audio.speedup(playback_speed=1.25)
faster_audio.export(output_file, format="mp3") 