class Music(str):
    id = "id"
    singer: str = "singer"
    song: str = "song"
    highest_pitch: str = "highest_pitch"
    lowest_pitch: str = "lowest_pitch"
    gender: int = "gender" # man:0, woman:1
    genre: str = "genre"
    key: int  = "key"