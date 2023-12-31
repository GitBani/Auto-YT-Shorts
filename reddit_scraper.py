import requests
from bs4 import BeautifulSoup


def _post_selector(tag):
    return tag.name == 'shreddit-post'  


def get_top_post(subreddit_url: str) -> str: 
    subreddit_url += 'top/'
    response = requests.get(subreddit_url) 
    html = response.text
    
    soup = BeautifulSoup(html, "html.parser")

    # body is 4 if there is a flair, else its 3
    posts = soup.find_all(_post_selector)
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
    return text
