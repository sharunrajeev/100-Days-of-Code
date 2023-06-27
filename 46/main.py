from pprint import pprint

from bs4 import BeautifulSoup as bs
from requests import get
from dotenv import load_dotenv
import spotipy

load_dotenv()
from spotipy.oauth2 import SpotifyOAuth
from os import environ as env

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=env['SPOTIPY_CLIENT_ID'],
    client_secret=env['SPOTIPY_CLIENT_SECRET'],
    scope='playlist-modify-public'
))

user_input = '2023-06-20'  # input("Which year do you want to travel to? Type the date in this format (YYYY-MM-DD) : ")
url = f"https://www.billboard.com/charts/hot-100/2023-06-20"

website_data = get(url)
soup = bs(website_data.content, 'html.parser')

# Get song titles from the billboard website
titles = soup.select(selector='.o-chart-results-list-row-container .lrv-u-width-100p #title-of-a-story')

# Create user playlist in spotify
playlist = sp.user_playlist_create(
    user=sp.current_user()['id'],
    name=f"[{user_input}] Billboard",
    description=f"Billboard Top 100 song of the week during the date {user_input}"
)

song_uris = []

for title in titles:
    song = sp.search(f'track:{title.getText().strip()} year:{user_input.split("-")[0]}', limit=1)
    song_uris.append(song['tracks']['items'][0]['uri'])

# Add playlist tracks
add_playlist = sp.playlist_add_items(
    playlist_id=playlist['id'],
    items=song_uris
)

print(add_playlist)
