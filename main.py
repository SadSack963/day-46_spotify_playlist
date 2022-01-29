import billboard_songs as bb
import spotipy_auth

"""
    Read ./Notes/Spotify - Create an App.odt
"""

# Get list of songs for a given date
date_reqd = input("What date do you want to go to? (YYYY-MM-DD): ")
list_songs = bb.get_song_titles(date_reqd)

# Create a Spotify Client
# AUTHORIZATION SCOPES: https://developer.spotify.com/documentation/general/guides/scopes/
sp = spotipy_auth.authorization_flow(scope="playlist-modify-private")
# print(dir(sp))

# Get current user details
user = sp.current_user()
# print(user)
user_id = user["id"]
print(f'{user_id = }')

# Create a Spotify Playlist and get the Playlist ID
playlist_name = f"Hot 100: {date_reqd}"
response = sp.user_playlist_create(
    user=user_id,
    name=playlist_name,
    public=False,
    collaborative=False,
    description='Hot 100 from billboard.com'
)
# print(response)
playlist_id = response["id"]
print(f'{playlist_id = }')

# Search Spotify for tracks and add the URI to list
year = date_reqd.split("-")[0]
song_uris = []
for song in list_songs:
    """
    Field Filters:
        album, artist, track, year (e.g. 1990 or 1990-2000), 
        tag, genre, upc (Universal Product Code), isrc (International Standard Recording Code)
        NOT excludes results
    """
    song_details = sp.search(
        q=f"track:{song}",  # year:{year}",
        limit=1,
        type="track",
        # market="from_token",
        market="GB",
    )
    print(f'song_details: \n{song_details}')  # see typical_song_details.py
    try:
        song_uri = song_details["tracks"]["items"][0]["uri"]
        # print(song_uri)
        song_uris.append(song_uri)
    except IndexError:
        print(f"{song} doesn't exist on Spotify.")

# Add tracks to Spotify Playlist
sp.playlist_add_items(
    playlist_id=playlist_id,
    items=song_uris,
    position=None
)
