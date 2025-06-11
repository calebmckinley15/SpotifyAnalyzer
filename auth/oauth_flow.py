# Authorization Flow Code for Spotify API

import os
import requests
import urllib.parse
from dotenv import load_dotenv

load_dotenv()

class SpotifyOAuth:
    def __init__(self):
        self.client_id = os.getenv('SPOTIFY_CLIENT_ID')
        self.client_secret = os.getenv('SPOTIFY_CLIENT_SECRET') 
        self.redirect_uri = os.getenv('SPOTIFY_REDIRECT_URI')
        self.scope = 'user-read-private user-read-email user-recently-played user-library-read user-top-read'
      
    def get_auth_url(self):
        base_url = 'https://accounts.spotify.com/authorize'
        params = {
            'client_id': self.client_id,
            'response_type': 'code',
            'redirect_uri': self.redirect_uri,
            'scope': self.scope
        }
        return f"{base_url}?{urllib.parse.urlencode(params)}"
    
    def get_token(self, auth_code):
        token_url = 'https://accounts.spotify.com/api/token'
        payload = {
            "grant_type": "authorization_code",
            "code": auth_code,
            "redirect_uri": self.redirect_uri,
            "client_id": self.client_id,
            "client_secret": self.client_secret 
        }

        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        response = requests.post(token_url, data=payload, headers=headers)
        if response.status_code != 200:
            raise Exception(f"Error fetching token: {response.text}")
        
        return response.json()
    