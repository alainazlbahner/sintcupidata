import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Define your credentials obtained from the Spotify Developer Dashboard
SPOTIPY_CLIENT_ID = 'your_client_id'
SPOTIPY_CLIENT_SECRET = 'your_client_secret'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'

scope = "user-read-playback-state"

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=scope))

def get_currently_playing():
    current_track = sp.current_playback()
    
    if current_track is not None and current_track['is_playing']:
        track_name = current_track['item']['name']
        artist_name = current_track['item']['artists'][0]['name']
        print(f"Currently playing: {track_name} by {artist_name}")
    else:
        print("No track is currently playing.")

if __name__ == "__main__":
    get_currently_playing()
