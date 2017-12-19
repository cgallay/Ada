import numpy as np
from scipy import stats
import pandas as pd
import hdf5_getters
import glob
from tqdm import tqdm_notebook as tqdm
import reverse_geocoder as rg

regex_half = {1:"[A-M]", 2:"[N-Z]"}

colsPart = {}
colsPart[1] = ['artist_latitude', 'artist_longitude', 'artist_terms', 'artist_terms_weight', 'year']
colsPart[2] = ['artist_hotttnesss', 'artist_name', 'artist_terms', 'artist_terms_weight',\
                   'loudness', 'song_hotttnesss', 'tempo', 'year', 'title',\
                  'X_mean', 'X_std', 'X_skew', 'X_kurtosis', 'X_median']

DIR_P = "./pickle_data/Filtered"
PATH_R = "../MillionSongData"
PATH_hdf5 = "./subset_msd_summary_file.h5"

def filter_year(df):
    #df[df.year >0] = np.nan
    return df[df["year"]!=0]#df.dropna(axis=0)

def filter_hotness(df_, threshold):
    df = df_.copy()
    assert threshold > 0 and threshold < 1, 'Threshold must be between 0 and 1'
    df = df.dropna(subset=['song_hotttnesss'])
    df['song_hotttnesss'] = df['song_hotttnesss'].astype(float)
    return df[df.song_hotttnesss > threshold]


def select_col(df, part):
    assert part in [1,2], 'part must be either 1 or 2'
    return df[colsPart[part]]

def exctract_timbre_features(df_original):
    df = df_original.copy()
    df['X_mean'] = df['segments_timbre'].apply(lambda m: np.mean(m, axis=0))
    df['X_std'] = df['segments_timbre'].apply(lambda m: np.std(m, axis=0))
    df['X_skew'] = df['segments_timbre'].apply(lambda m: stats.skew(m, axis=0))
    df['X_kurtosis'] = df['segments_timbre'].apply(lambda m: stats.kurtosis(m, axis=0))
    df['X_median'] = df['segments_timbre'].apply(lambda m: np.median(m, axis=0))
    return df

def save_pickle_filtered(df, letter, part, half):
    assert half in [1,2], "half must be either one or two"
    assert part in [1,2], "part must be either one to two"
    df.to_pickle(DIR_P + "/" + letter + "_part_" + str(part) + "_half_" + str(half) + ".pkl")

def read_pickle_filtered(letter, part, half):
    assert half in [1,2], "half must be either one or two"
    assert part in [1,2], "part must be either one to two"
    return pd.read_pickle(DIR_P + "/" + letter + "_part_" + str(part) + "_half_" + str(half) + ".pkl")

def load_song_data(letter, half):
    assert half in [1,2], 'half must be one or two'
    path = PATH_R
    categories = get_total_features()
    data = []
    file_paths = glob.glob(path+'/'+letter+'/'+regex_half[half]+'/*/*.h5')

    for file_path in tqdm(file_paths):
        h5file = hdf5_getters.open_h5_file_read(file_path)
        datapoint = {}
        for cat in categories:
            datapoint[cat] = getattr(hdf5_getters, "get_"+cat)(h5file)
        h5file.close()
        data.append(datapoint)

    df = pd.DataFrame(data)
    return df

def merge_pickles(letters, part):
    """
    Load and merge pickle
    :param letters:
    :param part:
    :return:
    """
    df_merged = pd.DataFrame(columns=colsPart[part])
    for letter in letters:
        for half in [1,2]:
            df = read_pickle_filtered(letter, part=part, half=half)
            df_merged = df_merged.append(df)
    return df_merged

def get_total_features():

    #Load the features name from the metadata into a list so that we don't have to insert them manually

    h5_summary = hdf5_getters.open_h5_file_read(PATH_hdf5)

    metadata = h5_summary.get_node('/metadata/songs/').colnames
    metadata.remove('genre')
    metadata.remove('analyzer_version')
    metadata = [w.replace('idx_', '') for w in metadata]

    analysis = h5_summary.get_node('/analysis/songs/').colnames
    analysis = [w.replace('idx_', '') for w in analysis]

    musicbrainz = h5_summary.get_node('/musicbrainz/songs/').colnames
    musicbrainz = [w.replace('idx_', '') for w in musicbrainz]

    total_features = np.array(metadata + analysis + musicbrainz).ravel()

    total_features = np.append(total_features, ['artist_terms_freq', 'artist_terms_weight', 'artist_mbtags_count'])


    total_features = np.sort(total_features)

    return total_features


# Map latitude/longitude to countries offline and completes Countries feature
def extend_countries(df):
    df_extended = df.copy()
    df_extended['Country'] = np.nan

    coordinates_bool = [not x for x in df.artist_latitude.isnull()]
    indexes_with_cordinates = df[coordinates_bool].index

    for ind in tqdm(indexes_with_cordinates):
        coord = (df["artist_latitude"][ind], df["artist_longitude"][ind])
        result = rg.search(coord)
        df_extended.loc[ind, 'Country'] = result[0]['cc']

    df_extended[['Country', 'title']].to_pickle('./temp/song_dataC', index=False)  # modify path if necessary

    return df_extended