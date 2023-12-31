from dotenv import load_dotenv
from random import randrange
import reddit_scraper
import tts


def main() -> None:
    load_dotenv()

    subreddits = ['https://www.reddit.com/r/AmItheAsshole/',
                  'https://www.reddit.com/r/UnethicalLifeProTips/',
                  'https://www.reddit.com/r/TalesFromRetail/', 
                ]
    random_subreddit_idx = randrange(0, len(subreddits))

    text = reddit_scraper.get_top_post(subreddits[random_subreddit_idx])

    tts.tts_rand_voice(text, 'speech.mp3')


if __name__ == '__main__':
    main()