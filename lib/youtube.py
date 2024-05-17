from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser

from lib.settings import YOUTUBE_API_KEY

YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_SERVICE_VERSION = 'v3'

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_SERVICE_VERSION, developerKey = YOUTUBE_API_KEY)




def crawl_youtube_image(singer, song):
    # q에 원하는 채널 이름 넣는다
    search_response = youtube.search().list(
        q=f"{singer}+{song}",
        order='relevance',
        part='snippet',
        maxResults=50,
    ).execute()

    youtube_image = search_response['items'][0]['snippet']['thumbnails']['default']['url']
    youtube_link = f"https://www.youtube.com/watch?v={search_response['items'][0]['id']['videoId']}"
    print(youtube_image, youtube_link)
    return youtube_image, youtube_link

