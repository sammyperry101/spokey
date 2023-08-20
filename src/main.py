import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import keys # Remove import
import get_data

def main():
    # Create auth manager and Spotify class for handing API calls
    auth_manager = SpotifyClientCredentials(client_id=get_data.SPOTIPY_CLIENT_ID, client_secret=get_data.SPOTIPY_CLIENT_SECRET)
    sp = spotipy.Spotify(auth_manager=auth_manager)

    tracks_api = get_data.apiCall(sp)

    tracks = get_data.getTrackIds(tracks_api)

    audio = get_data.getAudioFeatures(sp, tracks)

    # Combine dataframes
    tracks = pd.concat([tracks.reset_index(drop=True), audio.reset_index(drop=True)], axis=1)

    # Display dataframe
    print(tracks.to_string())

    # Name of filepath to save .csv to here
    tracks.to_csv("./data/tracks_example.csv", encoding="utf-16", index=False)

main()