# Wrapper for Spotify API

import requests

class SpotifyClient:
    def __init__(self, access_token):
        self.base_url = "https://api.spotify.com/v1"
        self.headers = {
            "Authorization": f"Bearer {access_token}"
        }

    def get_top_tracks(self, limit=25, time_range="medium_term"):
        url = f"{self.base_url}/me/top/tracks"
        params = {
            "limit": limit,
            "time_range": time_range
        }
        response = requests.get(url, headers=self.headers, params=params)
        if response.status_code != 200:
            raise Exception(f"Error fetching top tracks: {response.text}")
        
        return response.json()

    def get_top_artists(self, limit=25, time_range="medium_term"):
        url = f"{self.base_url}/me/top/artists"
        params = {
            "limit": limit,
            "time_range": time_range
        }

        response = requests.get(url, headers=self.headers, params=params)
        if response.status_code != 200:
            raise Exception(f"Error fetching top artists: {response.text}")
        
        return response.json()

    def get_recently_played(self, limit=50):
        url = f"{self.base_url}/me/player/recently-played"
        params = {
            "limit": limit
        }

        response = requests.get(url, headers=self.headers, params=params)
        if response.status_code != 200:
            raise Exception(f"Error fetching recently played tracks: {response.text}")
        
        return response.json()
    
    def get_playlist(self, playlist_id):
        url = f"{self.base_url}/playlists/{playlist_id}"
        response = requests.get(url, headers=self.headers)
        if response.status_code != 200:
            raise Exception(f"Error fetching playlist: {response.text}")
        
        return response.json()
    
    