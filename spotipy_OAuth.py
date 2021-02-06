import os
from dotenv import load_dotenv


load_dotenv("E:/Python/EnvironmentVariables/.env")
SPOTIPY_CLIENT_ID = os.getenv("Client_ID_Spotify")
SPOTIPY_CLIENT_SECRET = os.getenv("Client_Secret_Spotify")
SPOTIPY_REDIRECT_URI = os.getenv("Redirect_URI_Spotify")
SPOTIFY_BEARER_TOKEN = os.getenv("Bearer_Token_Spotify")

def client_credentials_flow():
    """
    Client Credentials Flow
        The Client Credentials flow is used in server-to-server authentication.
        Only endpoints that do not access user information can be accessed.
        The advantage here in comparison with requests to the Web API made without an access token,
        is that a higher rate limit is applied.

        As opposed to the Authorization Code Flow, you will not need to set SPOTIPY_REDIRECT_URI,
        which means you will never be redirected to the sign in page in your browser:
    """

    # Without user authentication
    # Example code from https://pypi.org/project/spotipy/

    import spotipy
    from spotipy.oauth2 import SpotifyClientCredentials

    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID,
                                                               client_secret=SPOTIPY_CLIENT_SECRET))

    results = sp.search(q='weezer', limit=20)
    for index, track in enumerate(results['tracks']['items']):
        print(index, track['name'])


def authorization_flow(scope):
    """
    Authorization Code Flow
        This flow is suitable for long-running applications in which the user grants permission only once.
        It provides an access token that can be refreshed. Since the token exchange involves sending your secret key,
        perform this on a secure location, like a backend service, and not from a client such as a browser
        or from a mobile app.

    Redirect URI
        The Authorization Code Flow needs you to add a redirect URI to your application at My Dashboard
        (navigate to your application and then [Edit Settings]).
        The redirect_uri argument or SPOTIPY_REDIRECT_URI environment variable must match the redirect URI added
        to your application in your Dashboard. The redirect URI can be any valid URI (it does not need to be accessible)
        such as http://example.com, http://localhost or http://127.0.0.1:9090.
    """

    # With user authentication
    # Example code from https://pypi.org/project/spotipy/

    import spotipy
    from spotipy.oauth2 import SpotifyOAuth

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                                   client_secret=SPOTIPY_CLIENT_SECRET,
                                                   redirect_uri=SPOTIPY_REDIRECT_URI,
                                                   scope=scope))

    results = sp.current_user_saved_tracks()
    print(sp.current_user())

    for index, item in enumerate(results['items']):
        track = item['track']
        print(index, track['artists'][0]['name'], " – ", track['name'])


"""
IDs URIs and URLs

Spotipy supports a number of different ID types:

        Spotify URI - The resource identifier that you can enter, for example, in the Spotify Desktop client’s search box to locate an artist, album, or track. Example: spotify:track:6rqhFgbbKwnb9MLmUQDhG6
        Spotify URL - An HTML link that opens a track, album, app, playlist or other Spotify resource in a Spotify client. Example: http://open.spotify.com/track/6rqhFgbbKwnb9MLmUQDhG6
        Spotify ID - A base-62 number that you can find at the end of the Spotify URI (see above) for an artist, track, album, etc. Example: 6rqhFgbbKwnb9MLmUQDhG6


"""