from dotenv import load_dotenv
from src.models import SpotifyWrapper

def main():
    spotify_api = SpotifyWrapper()
    playlist_detail = spotify_api.get_playlist('6BTQk5h0RoJGAo8kGY7tYQ')
    print(playlist_detail)

if __name__ == "__main__":
    load_dotenv()
    main()
