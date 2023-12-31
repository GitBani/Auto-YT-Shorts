# Automated YouTube Shorts
This project intends to automate the process of creating TTS videos of trending Reddit posts, with some unrelated satisfying video in the background.

1. Use beautifulSoup to parse the html I request to find a post that is trending in some selected subreddit
2. With the text, I use OpenAI/gTTS/TikTok TTS to generate the audio
3. I select a random clip of equal length to the audio from pre-downloaded satisfying videos
4. I place the audio over the clip with captions
5. Hopefully, I can send a request to automatically post the video

## TODO FIX
1. Deal with bodyless posts, maybe get top comment.
2. Deal with posts that don't have any flair