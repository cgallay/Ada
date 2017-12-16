import requests
import base64
import re
client_id = ''
client_secret = ''


class spotify:


    def __init__(self):

        self.token = self.get_access_token(client_id, client_secret)

    def get_access_token(self, id, secret):
        url = 'https://accounts.spotify.com/api/token'
        payload = {'grant_type':'client_credentials'}

        credentials = id + ':' + secret
        headers = {
        'Authorization': 'Basic ' + base64.b64encode(credentials.encode()).decode()
        }

        r = requests.post(url, data=payload, headers=headers)

        return r.json()['access_token']

    def search(self, search, type):


        #GET "https://api.spotify.com/v1/search?q=tania*&type=artist" -H "Authorization: Bearer {your access token}"
        url2 = "https://api.spotify.com/v1/search"

        payload2 = {'q': search, 'type': type}

        headers2 = {'Authorization': 'Bearer '+ self.token}
        res = requests.get(url2, params=payload2, headers=headers2)

        return res.json()

    def search_preview(self, artist, track, show=False):

        show = show
        artists = []

        url = "https://api.spotify.com/v1/search"
        headers = {'Authorization': 'Bearer '+ self.token}

        all_artist = re.split(',| & | / | /|/ |/| feat. | featuring | feat ', artist)

        for artist in all_artist:

            artist_result = requests.get(url, params={'q': artist, 'type': 'artist'}, headers=headers)
            artist_json = artist_result.json()
            for artist in artist_json['artists']['items']:
                artists.append(artist['name'])


        track_result = requests.get(url, params={'q': track, 'type': 'track'}, headers=headers)
        track_json = track_result.json()

        for album in track_json['tracks']['items']:
            for artist in album['artists']:
                if(show):
                    print(artist['name'])
                    print(album['preview_url'])
                if artist['name'] in artists:
                    if album['preview_url'] is not None:
                        return album['preview_url']

        return None
