import requests
from dotenv import load_dotenv
import os
from src.models import SpotifyWrapper

def main():
    spotify_api = SpotifyWrapper()
    playlist_detail = spotify_api.get_playlist_of_user('3cEYpjA9oz9GiPac4AsH4n')
    print(playlist_detail)

if __name__ == "__main__":
    load_dotenv()
    main()
