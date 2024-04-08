from typing import List, Any

from lib.database.mysql.mysql import Connection


def create_music_in_mysql(data):
    query = "INSERT INTO music (singer, song, highest_pitch, lowest_pitch, gender) VALUES (%s, %s, %s, %s, %s)"
    conn = Connection()
    conn.save_all(query, data)