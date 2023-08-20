import pandas as pd
import spotipy
import key_conversions
import keys

# Define constants - set own credentials upon download
SPOTIPY_CLIENT_ID = keys.SPOTIPY_CLIENT_ID # Set own Spotify Client ID here
SPOTIPY_CLIENT_SECRET = keys.SPOTIPY_CLIENT_SECRET # Set own Spotify Client Secret
PLAYLIST_ID = 'spotify:playlist:7wsEUldS5ZU2UDAMZealYG' # Set own Spotify Playlist ID

# Constants used when querying API
AUDIO_FEATURES_QUERY_SIZE = 100
TRACKS__QUERY_SIZE = 50

# Main API call to fetch track information for playlist_id
def apiCall(sp : spotipy.Spotify) -> list:
    # Define loop variables
    offset = 0
    tracks_api = []
    names = []

    # Call API to receive track information for all songs in a playlist (receive 100 at a time)
    while True:
        response = sp.playlist_tracks(PLAYLIST_ID,
                                    offset=offset,
                                    fields='items.track.id, items.track.name')
        
        name_response = sp.playlist_tracks(PLAYLIST_ID,
                                    offset=offset,
                                    fields='items.track.name')

        if len(response['items']) == 0:
            break
        
        tracks_api.extend(response['items'])
        names.extend(name_response['items'])
        offset = offset + len(response['items'])

    return tracks_api

# Get Track IDs from API call results
def getTrackIds(tracks_api : list) -> pd.DataFrame:
    tracks = []

    # Loop through returned data to gather track ids
    for track in tracks_api:
        track = eval(str(track))
        item = {"id" : track['track']['id'], "name" : track['track']['name']}
        tracks.append(item)

    tracks = pd.DataFrame(tracks)

    return tracks

# Get audio features from tracks
def getAudioFeatures(sp : spotipy.Spotify, tracks : pd.DataFrame) -> pd.DataFrame:
    audio_features = []

    # Read all audio features (in batches of 100 ids)
    start_read = 0
    while start_read < len(tracks):
        end_read = min(len(tracks) - start_read, AUDIO_FEATURES_QUERY_SIZE)
        response = sp.audio_features(list(tracks[start_read : start_read + end_read]["id"]))

        audio_features.extend(response)

        start_read += end_read

    audio = []

    # Loop through returned data to gather audio feature information
    for track_features in audio_features:
        track_features = eval(str(track_features))
        item = {"key" : track_features['key'], "mode" : track_features['mode'], "tempo" : track_features['tempo']}

        item = key_conversions.keyIntToNote(item)
        item = key_conversions.modeIntToNote(item)
        
        audio.append(item)

    audio = pd.DataFrame(audio)

    return audio