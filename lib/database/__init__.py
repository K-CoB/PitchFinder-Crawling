# -*- coding: utf-8 -*-
from lib.database.mysql.mysql import Connection
from lib.youtube import crawl_youtube_image
from googleapiclient.errors import HttpError


def create_music_in_mysql(data):
    query = "INSERT INTO music (song, singer, highest_pitch, lowest_pitch, gender, youtube_url) VALUES (%s, %s, %s, %s, %s, %s)"
    conn = Connection()
    data = [tuple(d.values()) for d in data]
    conn.save_all(query, data)



def update_youtube_image_url():
    conn = Connection()
    data = conn.select_all('SELECT * FROM music')
    tmp = []
    try:
        for d in data:
            thumbnail, youtube_link = crawl_youtube_image(d['singer'], d['song'])
            song_data = {
                "title": d['song'],
                "singer": d['singer'],
                # "high": d['high'],
                # "low": d['low'],
                # "gender": d['gender'],
                "youtube_url": youtube_link,
                "thumbnail": thumbnail
            }
            tmp.append(song_data)
    except HttpError:
        print("quota error")
        print(tmp)
    return tmp

def update_music(data):
    query = "UPDATE music SET youtube_listen_url = %s WHERE singer = %s AND song = %s"
    conn = Connection()
    data = [tuple([d['youtube_url'], d['singer'], d['title']]) for d in data]
    conn.save_all(query, data)



