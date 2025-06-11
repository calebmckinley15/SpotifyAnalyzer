# Script to get user data from Spotify API

import json
import auth.spotify_client as SpotifyClient
import auth.oauth_flow as SpotifyOAuth

def main():
        authenticor = SpotifyOAuth()
        auth_code = input("Paste your authorization code from redirect URL: ")
        token_data = authenticor.get_token(auth_code)

        access_token = token_data['access_token']
        client = SpotifyClient(access_token)

        top_tracks = client.get_top_tracks(limit=25)
        with open("data/top_tracks.json", "w") as f:
                json.dump(top_tracks, f, indent=4)

        top_artists = client.get_top_artists(limit=25)
        with open("data/top_artists.json", "w") as f:
                json.dump(top_artists, f, indent=4)

        recently_played = client.get_recently_played(limit=50)
        with open("data/recently_played.json", "w") as f:
                json.dump(recently_played, f, indent=4)
        
if __name__ == "__main__":
    main()
    