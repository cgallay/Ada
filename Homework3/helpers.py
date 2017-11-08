from folium import plugins
import pandas as pd
import folium
import branca

swiss_topo = r'topojson/ch-cantons.topojson.json' # type: str

def add_swiss_topo(m, style_function=None):
    folium.TopoJson(open(swiss_topo),
                   'objects.cantons',
                    name="my name",
                   style_function=style_function).add_to(m)

def add_swiss_map(m, df: pd.DataFrame, colorscale):
    serie = df.set_index("Canton_abv")["Taux de chômage"]
    def style_function(feature):
        rate = serie.get(feature['id'], None)
        return {
            'fillOpacity': 0.5,
            'weight': 1,
            'fillColor': '#black' if rate is None else colorscale(rate)
        }
    add_swiss_topo(m, style_function)

    return m

def create_swiss_map(df: pd.DataFrame, column: str) -> folium.Map:
    """
    create a map of switzerland
    """

    m = folium.Map([46.8734, 8.2200], zoom_start=8)
    plugins.ScrollZoomToggler().add_to(m)
    m.choropleth(
        geo_data=open(swiss_topo),
        topojson='objects.cantons',
        data=df,
        columns=['Canton_abv', column],
        key_on='id',
        fill_color='YlOrRd', fill_opacity=0.7, line_opacity=0.2,
        legend_name='Unemployment Rate (%)',
        reset=True)
    return m


dic_can_to_pos = {
    "BE": [46.950262, 7.426758],
    "SO": [47.20709, 7.53972],
    "BL": [47.451702, 7.702241],
    "BS": [47.548801, 7.58781],
    "AG": [47.409843, 8.156862],
    "ZH": [47.384514, 8.524655],
    "GL": [47.039951, 9.06806],
    "SH": [47.721916, 8.564374],
    "AR": [47.366154, 9.361339],
    "AI": [47.331429, 9.40768],
    "SG": [47.23045, 9.271915],
    "GR": [46.656055, 9.628635],
    "TG": [47.568668, 9.089865],
    "LU": [47.067936, 8.110318],
    "UR": [46.771984, 8.628699],
    "SZ": [47.061832, 8.756658],
    "OW": [46.858185, 8.208873],
    "NW": [46.9268, 8.405315],
    "ZG": [47.157269, 8.5373],
    "VD": [46.573967, 6.481934],
    "VS": [46.209427, 7.605942],
    "GE": [46.202409, 6.144447],
    "FR": [46.708508, 7.096611],
    "NE": [46.995552, 6.780256],
    "JU": [47.361799, 7.196443],
    "TI": [46.247166, 8.880489]

}