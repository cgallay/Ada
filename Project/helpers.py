from tqdm import tqdm
from spotify import *

topic2genre = {0:'Raggae', 1:'Pop', 2:'Jazz', 3:'Rock', 4:'Blues', 5:'Latin', 6:'Electronic', 7:'Country', 8:'Metal', 9:'Rap'}

def add_previews_spotify(df, path=None):

    spot = spotify()
    df_previews = df.copy()
    df_previews['preview_url'] = 0
    tracks = {}

    for ind in tqdm(range(0, len(df_previews))):
        track = df_previews.loc[ind, ['artist_name', 'title', 'track_id']]
        try:
            tracks[track[2]] = spot.search_preview(track[0], track[1])
        except Exception:
            tracks[track[2]] = None

    df_previews = df_previews.set_index('track_id')

    for key in tqdm(tracks.keys()):

        df_previews.loc[key, 'preview_url'] = tracks[key]

    df_previews = df_previews.reset_index()

    if (path):
        df_previews.to_pickle(path)

    return df_previews

def add_previews_deezer(df, path=None):

    df_previews = df.copy()
    df_previews['preview_url'] = 0
    tracks = {}

    for ind in tqdm(range(0, len(df_previews))):

        track = df_previews.loc[ind, ['artist_name', 'title', 'track_id']]
        try:
            tracks[track[2]] = search_deezer(track[0], track[1])
        except Exception:
            tracks[track[2]] = None


    df_previews = df_previews.set_index('track_id')

    for key in tqdm(tracks.keys()):

        df_previews.loc[key, 'preview_url'] = tracks[key]

    df_previews = df_previews.reset_index()

    if (path):
        df_previews.to_pickle(path)

    return df_previews


def search_deezer(artist, title):

    url = 'https://api.deezer.com/search?q='

    url_artist = 'artist:'+'"'+artist+'"'

    url_track = 'track:'+'"'+title+'"'

    res_track = requests.get(url + url_artist + url_track).json()['data']

    if len(res_track)==0:

        track = re.split(" \(" , title)[0]
        url = url + url_artist+ 'track:' + '"' + track + '"'
        res_track = requests.get(url).json()['data']

    return res_track[0]['preview']

def complete_previews(df_deezzer, df_spotify, path=None):
    df_deezzer = df_deezzer.copy()
    df_spotify = df_spotify.copy()
    None_indexes = df_deezzer[[x is None for x in df_deezzer.preview_url]].set_index('track_id')
    df_deezzer = df_deezzer.set_index('track_id')
    df_spotify = df_spotify.set_index('track_id')
    added = 0
    for x in None_indexes.index:
        extra = df_spotify.loc[x, 'preview_url']
        if (extra is not None):
            df_deezzer.loc[x, 'preview_url'] = extra
            added += 1

    if(path):
        df_deezzer.to_pickle(path)
    print(added, ' entries were added')
    return  df_deezzer

