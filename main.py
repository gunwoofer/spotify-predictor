import spotipy
import spotipy.util as util
from json.decoder import JSONDecodeError
import config

print (" -- Initialisation Main : Spotify-Predictor -- ")

username = config.SPOTIPY_CONFIG['username']
scope = config.SPOTIPY_CONFIG['scope']

def main():
    try:
        token = util.prompt_for_user_token(username, scope)
        spotify = spotipy.Spotify(auth=token)
        
        playlists = spotify.current_user_playlists()
        print(playlists)
    except (AttributeError, JSONDecodeError):
        # Renouvellement du token
        os.remove(f".cache-{username}")
        token = util.prompt_for_user_token(username, scope)



if __name__ == "__main__":
    main()



