import requests
import os

class SpotifyWrapper:
    def __init__(self):
        self.client_id = os.getenv('SPOTIFY_CLIENT_ID')
        self.client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
        self.update_access_token(self.client_id, self.client_secret)

    def update_access_token(self, client_id, client_secret):
        auth_url = 'https://accounts.spotify.com/api/token'

        auth_data = {
            'grant_type': 'client_credentials',
            'client_id': client_id,
            'client_secret': client_secret
        }
        
        auth_response = requests.post(auth_url, data=auth_data)
        
        if auth_response.status_code == 200:
            self.access_token = auth_response.json()['access_token']
            print(f"アクセストークンを更新しました: {self.access_token}")
            return auth_response.json()
        else:
            raise Exception(f"認証エラー: {auth_response.status_code}")

    def get_artist_info(self, artist_id):
        headers = {
            'Authorization': f'Bearer {self.access_token}'
        }
        url = f'https://api.spotify.com/v1/artists/{artist_id}'

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"アーティスト情報の取得に失敗しました: {response.status_code}")

    def get_playlist_of_user(self, spotify_id):
        headers = {
            'Authorization': f'Bearer {self.access_token}'
        }
        url = f'https://api.spotify.com/v1/playlists/{spotify_id}'

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"プレイリストの取得に失敗しました: {response.status_code}")

