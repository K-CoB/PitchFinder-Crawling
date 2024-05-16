import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from lib.settings import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET

client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

print(sp.search(q='artist:강성%20'))

# def add_spotify_api(data):
#