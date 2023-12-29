from bs4 import BeautifulSoup
from urllib.request import urlopen
# from dotenv import load_dotenv
from gtts import gTTS
from pydub import AudioSegment


url = "https://www.reddit.com/r/AmItheAsshole/top/"#'https://www.reddit.com/r/UnethicalLifeProTips/top/'#'https://www.reddit.com/r/Showerthoughts/top/'#
outputfile = 'speech.mp3'


MAX_POST_LENGTH = 1250 # to keep video length under 1 minute


page = urlopen(url)
html = page.read().decode("utf-8")


soup = BeautifulSoup(html, "html.parser")


def post_selector(tag):
    return tag.name == 'shreddit-post'  


posts = soup.find_all(post_selector)
link_with_post_title = posts[1].find_all('a')[0]
link_with_post_body = posts[1].find_all('a')[4]

title = link_with_post_title.attrs.get('aria-label')


body = ""
for paragraph in link_with_post_body.find_all('p'):
    body += paragraph.getText()


text = title + body
text = text.replace('AITA', 'Am I the A-hole')
text = text.replace('ULPT', 'Unethical life pro tip')
text = text.replace('\n', '')
tts = gTTS(text=text, lang='en')
tts.save(outputfile)
print(len(text))


audio = AudioSegment.from_file(outputfile, format="mp3")
faster_audio = audio.speedup(playback_speed=1.5)
faster_audio.export(outputfile, format="mp3") 