# SpoKey
SpoKey (or Spotify Key) is a Python Script to query the Spotify API to get the key and tempo of all pieces in a Spotify playlist.

This project allows for you to select any Spotify playlist and create a .csv file containing the key, mode and tempo of all songs in the playlist. This can allow for functionality such as easily seeing which songs could blend together well for creating mixes or dj sets.

## Setup:
To set up this project, you will need to generate SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET environment variables. A guide on how to do this can be seen [here](https://www.youtube.com/watch?v=kaBVN8uP358&t=0s).

Once these values have been got, these can be set in a new file named keys.py in the src folder using the following format:
```
SPOTIPY_CLIENT_ID = 'Your-Spotipy-Client-ID'
SPOTIPY_CLIENT_SECRET = 'Your-Spotipy-Client-Secret' 
```

If you have any issues/questions, please reach out to sammy2580@hotmail.com
