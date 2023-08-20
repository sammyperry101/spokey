import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import keys # Remove import

# Define constants - set own credentials upon download
SPOTIPY_CLIENT_ID = keys.SPOTIPY_CLIENT_ID
SPOTIPY_CLIENT_SECRET = keys.SPOTIPY_CLIENT_SECRET
PLAYLIST_ID = 'spotify:playlist:7wsEUldS5ZU2UDAMZealYG'

AUDIO_FEATURES_QUERY_SIZE = 100
TRACKS__QUERY_SIZE = 50

def keyIntToNote(item):
    if item["key"] == 0:
        item["key"] = "C"
    elif item["key"] == 1:
        item["key"] = "C#/D♭"
    elif item["key"] == 2:
        item["key"] = "D"
    elif item["key"] == 3:
        item["key"] = "D#/E♭"
    elif item["key"] == 4:
        item["key"] = "E"
    elif item["key"] == 5:
        item["key"] = "F"
    elif item["key"] == 6:
        item["key"] = "F#/G♭"
    elif item["key"] == 7:
        item["key"] = "G"
    elif item["key"] == 8:
        item["key"] = "G#/A♭"
    elif item["key"] == 9:
        item["key"] = "A"
    elif item["key"] == 10:
        item["key"] = "A#/B♭"
    elif item["key"] == 11:
        item["key"] = "B"

    return item

def modeIntToNote(item):
    if item["mode"] == 0:
        item["mode"] = "Minor"
    elif item["mode"] == 1:
        item["mode"] = "Major"

    return item

# Create auth manager and Spotify class for handing API calls
auth_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

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

tracks = []

# Loop through returned data to gather track ids
for track in tracks_api:
    track = eval(str(track))
    item = {"id" : track['track']['id'], "name" : track['track']['name']}
    tracks.append(item)

tracks = pd.DataFrame(tracks)

print(tracks)

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

    item = keyIntToNote(item)
    item = modeIntToNote(item)
    
    audio.append(item)

audio = pd.DataFrame(audio)

# Combine dataframes
tracks = pd.concat([tracks.reset_index(drop=True), audio.reset_index(drop=True)], axis=1)

print(tracks)

tracks.to_csv("./tracks_example.csv", encoding="utf-16", index=False)