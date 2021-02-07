import os
from dotenv import load_dotenv


SPOTIFY_BEARER_TOKEN = os.getenv("Bearer_Token_Spotify")


# Albums API
# ==========

# Get Multiple Albums
def get_multiple_albums():
    """
    Get Spotify catalog information for multiple albums identified by their Spotify IDs.

    This endpoint requires authentication, but does not require a specific scope.

    :return:
    On success, the HTTP status code in the response header is 200 OK and the response body contains an object whose key is "albums" and whose value is an array of album objects in JSON format.
    Objects are returned in the order requested. If an object is not found, a null value is returned in the appropriate position. Duplicate ids in the query will result in duplicate objects in the response. On error, the header status code is an error code and the response body contains an error object.
    """

    endpoint_url = "https://api.spotify.com/v1/albums"
    header = {
        "Authorization": f"Bearer {SPOTIFY_BEARER_TOKEN}",  # Required - A valid user access token or your client credentials.
        "Accept": "application / json",
        "Content-Type": "application / json",
    }
    query = {
        "ids": "6icDB6wt9kle4AkCoPAtaZ",  # Required - A comma-separated list of the Spotify IDs for the albums. Maximum: 20 IDs.
        "market": "GB",  # Optional - An ISO 3166-1 alpha-2 country code or the string from_token. Provide this parameter if you want to apply Track Relinking.
    }


# Get an Album
def get_album():
    """
    Get Spotify catalog information for a single album.

    :return:
    On success, the HTTP status code in the response header is 200 OK and the response body contains an album object in JSON format. On error, the header status code is an error code and the response body contains an error object.
    """

    album_id = "6icDB6wt9kle4AkCoPAtaZ",  # Required - The Spotify ID of the album.

    endpoint_url = f"https://api.spotify.com/v1/albums/{album_id}"  # The Spotify ID of the album.
    header = {
        "Authorization": f"Bearer {SPOTIFY_BEARER_TOKEN}",  # Required - A valid user access token or your client credentials.
        "Accept": "application / json",
        "Content-Type": "application / json",
    }
    query = {
        "market": "GB",  # Optional - An ISO 3166-1 alpha-2 country code or the string from_token. Provide this parameter if you want to apply Track Relinking.
    }


# Get an Album's Tracks
def get_album_tracks():
    """
    Get Spotify catalog information about an album’s tracks.

    Optional parameters can be used to limit the number of tracks returned

    :return:
    On success, the HTTP status code in the response header is 200 OK and the response body contains an album object in JSON format. On error, the header status code is an error code and the response body contains an error object.
    """

    album_id = "6icDB6wt9kle4AkCoPAtaZ",  # Required - The Spotify ID of the album.

    endpoint_url = f"https://api.spotify.com/v1/albums/{album_id}/tracks"  # The Spotify ID of the album.
    header = {
        "Authorization": f"Bearer {SPOTIFY_BEARER_TOKEN}",  # Required - A valid user access token or your client credentials.
        "Accept": "application / json",
        "Content-Type": "application / json",
    }
    query = {
        "market": "GB",  # Optional - An ISO 3166-1 alpha-2 country code or the string from_token. Provide this parameter if you want to apply Track Relinking.
        "limit": 20,  # Optional - The maximum number of tracks to return. Default: 20. Minimum: 1. Maximum: 50.
        "offset": 0,  # Optional - The index of the first track to return. Default: 0 (the first object). Use with limit to get the next set of tracks.
    }


# Playlists API
# =============

# Create a Playlist
def create_playlist():
    """
    Create a playlist for a Spotify user. (The playlist will be empty until you add tracks.)

    :return:
    On success, the response body contains the created playlist object in JSON format and the HTTP status code in the response header is 200 OK or 201 Created. There is also a Location response header giving the Web API endpoint for the new playlist.
    On error, the header status code is an error code and the response body contains an error object. Trying to create a playlist when you do not have the user’s authorization returns error 403 Forbidden.
    """

    user_id = "#####"  # The user’s Spotify user ID.

    endpoint_url = f"https://api.spotify.com/v1/users/{user_id}/playlists"  #
    header = {
        "Authorization": f"Bearer {SPOTIFY_BEARER_TOKEN}",  # Required - A valid user access token or your client credentials.
        "Accept": "application / json",
        "Content-Type": "application / json",
    }
    query = {
        "name": "",  # The name for the new playlist, does not need to be unique.
        "public": "",  # Defaults to true . To create private playlists, the user must have granted the playlist-modify-private scope
        "collaborative": "",  # Defaults to false . To create a collaborative playlist you must also set public to false. You must have granted playlist-modify-private and playlist-modify-public scopes .
        "description": "",  # Playlist description as displayed in Spotify Clients and in the Web API.
    }


# Users Profile API
# =================

# Get Current User's Profile
def get_current_user_profile():
    """
    Get detailed profile information about the current user (including the current user’s username).

    :return:
    On success, the HTTP status code in the response header is 200 OK and the response body contains a user object in JSON format. On error, the header status code is an error code and the response body contains an error object. When requesting fields that you don’t have the user’s authorization to access, it will return error 403 Forbidden.
    Important! If the user-read-email scope is authorized, the returned JSON will include the email address that was entered when the user created their Spotify account. This email address is unverified; do not assume that the email address belongs to the user.

    """

    endpoint_url = f"https://api.spotify.com/v1/me"  #
    header = {
        "Authorization": f"Bearer {SPOTIFY_BEARER_TOKEN}",  # Required - A valid user access token or your client credentials.
        "Accept": "application / json",
        "Content-Type": "application / json",
    }


