from typing import List, Any

from lib.database.mysql.mysql import Connection


def create_music_in_mysql(data):
    query = "INSERT INTO music (song, singer, highest_pitch, lowest_pitch, gender, youtube_url) VALUES (%s, %s, %s, %s, %s, %s)"
    conn = Connection()
    data = [tuple(d.values()) for d in data]
    print(data)
    conn.save_all(query, data)
