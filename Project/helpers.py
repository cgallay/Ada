from tqdm import tqdm
import spotify

topic2genre = {0:'Raggae', 1:'Pop', 2:'Jazz', 3:'Rock', 4:'Blues', 5:'Latin', 6:'Electronic', 7:'Country', 8:'Metal', 9:'Rap'}


def add_previews_spotify(df, path=None):
    spot = spotify.spotify()
    df_previews = df.copy()
    tracks = {}

    for ind in tqdm(range(0, len(df_previews))):
        try:
            track = df_previews.loc[ind, ['artist_name', 'title', 'track_id']]
            tracks[track[2]] = spot.search_preview(track[0], track[1])
        except Exception:
            print(track)

    df_previews['preview_url'] = 0
    df_previews = df_previews.set_index('track_id')

    for key in tqdm(tracks.keys()):
        df_previews.loc[key, 'preview_url'] = tracks[key]

    df_previews = df_previews.reset_index()

    if (path):
        df_previews.to_pickle(path)

    return df_previews