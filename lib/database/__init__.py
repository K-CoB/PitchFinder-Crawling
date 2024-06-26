# -*- coding: utf-8 -*-
from lib.database.mysql.mysql import Connection
from lib.youtube import crawl_youtube_image, crawl_youtube_tj
from googleapiclient.errors import HttpError


def create_music_in_mysql(data):
    query = "INSERT INTO music (song, singer, highest_pitch, lowest_pitch, gender, youtube_image, youtube_url) VALUES (%s, %s, %s, %s, %s, %s)"
    conn = Connection()
    data = [tuple(d.values()) for d in data]
    conn.save_all(query, data)


def update_youtube_image_url():
    conn = Connection()
    data = conn.select_all('SELECT * FROM music WHERE id>210')
    tmp = []
    try:
        for d in data:
            thumbnail, youtube_link = crawl_youtube_image(d['singer'], d['song'])
            youtube_sing_url = crawl_youtube_tj(d['singer'], d['song'])
            song_data = {
                "title": d['song'],
                "singer": d['singer'],
                "youtube_listen_url": youtube_link,
                "thumbnail": thumbnail,
                "youtube_sing_url": youtube_sing_url
            }
            tmp.append(song_data)
    except HttpError:
        print("quota error")
        print(tmp)
    return tmp

def update_music(data):
    query = "UPDATE music SET youtube_url = %s, youtube_image = %s, youtube_listen_url = %s WHERE singer = %s AND song = %s"
    conn = Connection()
    data = [tuple([d['youtube_listen_url'],d['thumbnail'],d['youtube_sing_url'], d['singer'], d['title']]) for d in data]
    conn.save_all(query, data)