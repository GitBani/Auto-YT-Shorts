from bs4 import BeautifulSoup
from urllib.request import urlopen
from dotenv import load_dotenv

url = "https://www.reddit.com/r/AmItheAsshole/top/"


try:
    page = urlopen(url)
    html = page.read().decode("utf-8")
except:
    exit(-1)


soup = BeautifulSoup(html, "html.parser")


def post_selector(tag):
    return tag.name == 'shreddit-post'  


posts = soup.find_all(post_selector)
link_with_post_title = posts[0].find_all('a')[0]
link_with_post_body = posts[0].find_all('a')[4]


title = link_with_post_title.attrs.get('aria-label')


text = ""
for paragraph in link_with_post_body.find_all('p'):
    text += paragraph.getText()

print(title + text)
print(len(title + text))