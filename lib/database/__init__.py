from typing import List, Any

from lib.database.mysql.mysql import Connection
from lib.youtube import crawl_youtube_image


def create_music_in_mysql(data):
    query = "INSERT INTO music (song, singer, highest_pitch, lowest_pitch, gender, youtube_url) VALUES (%s, %s, %s, %s, %s, %s)"
    conn = Connection()
    data = [tuple(d.values()) for d in data]
    print(data)
    conn.save_all(query, data)



def update_youtube_image_url(data):
    for i in range(len(data)):
        thumbnail = crawl_youtube_image(data[i]['singer'], data[i]['song'])
        data[i]['thumbnail'] = thumbnail
    print(data)

conn = Connection()
update_youtube_image_url(conn.select_all('SELECT * FROM music'))