import billboard_songs as bb
import spotipy_OAuth


# Get list of songs for a given date
list_songs = bb.get_song_titles()

# Get Spotify Authorization
spotipy_OAuth.authorization_flow(scope="playlist-modify-private user-read-private")
