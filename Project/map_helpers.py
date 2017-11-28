import pandas as pd

import folium
import folium.plugins as plugins

def artistDensityMap(df):
    """Return a HeatMap of the world showing the artist location
    
    parms:
        df: DataFrame must contain columns ["artist_latitude", "artist_longitude"]
    """
    m = folium.Map([48., 5.], tiles='stamentoner', zoom_start=2)
    hm = plugins.HeatMap(df[["artist_latitude", "artist_longitude"]].values.tolist(), radius=15)
    hm.add_to(m)
    return m

def extendsData(df):
    """Add weight to the songs location which decrease through time
    
    params:
        df: DataFrame with columns ['artist_latitude', 'artist_longitude', 'year']
        
    Return:
        A DataFrame with columns ['artist_latitude', 'artist_longitude', 'weight', 'year']
    """
    nb_years = 10
    new_df = []
    for i, row in df.iterrows():
        for j in range(nb_years):
            w = 1 - j/nb_years
            new_row = [row['artist_latitude'], row['artist_longitude'], w, row["year"] + j]
            new_df.append(new_row)
            
    return pd.DataFrame(new_df, columns=['artist_latitude', 'artist_longitude', 'weight', 'year'])

def showMapWithTime(df):
    df["weight"] = 1
    return showMapWithTimeAndWeight(df)

def showMapWithTimeAndWeight(df, radius=15, htmlFilename= 'myMap.html'):
    """Show a HeatMap representing artist density on earth per year
    
    params:
        df: DataFrame with columns ['artist_latitude', 'artist_longitude', 'weight']
            weight must be contain between 0 and 1 ([0,1]) 
        radius: Size of each point on the map
        htmlFilename: Location on the disc where to store the map 
    """
    m = folium.Map([48., 5.], tiles='stamentoner', zoom_start=2)
    df = df.sort_values("year")

    data = df.groupby("year")[['artist_latitude', 'artist_longitude', "weight"]].apply(lambda df_ : df_.values.tolist()).tolist()
    index = df.year.astype(str).unique().tolist()
    assert len(data) == len(index)
    hm = plugins.HeatMapWithTime(data, index=index, radius=radius)
    hm.add_to(m)
    
    if htmlFilename:
        m.save(htmlFilename)

    return m

def selectData(df):
    """Select column of interest for map vizualization add drop rows with missing values
    
    parms:
        df: DataFrame must containst ["artist_latitude", "artist_longitude", "title", "year"]
    """
    df = df[df["year"]!=0]
    df = df[["artist_latitude", "artist_longitude", "title", "year"]].dropna()
    return df

def selectGenre(df, genre):
    """Select only genre of interest and complete value by calling methode :func:`~selectData()`
    
    params:
        df: Original dataFrame from which the data comes
        genre: The genre id ranging from 0 to the number of topic on which the LDA was trained
    """
    df = df[df["genre"] == genre]
    return selectData(df)