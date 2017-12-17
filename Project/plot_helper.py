import plotly.graph_objs as go
import plotly.plotly as py
import plotly
import numpy as np
from helpers import *
import matplotlib
import matplotlib.pyplot as plt


def scatter_plot(data, genre, infos=None, urls=None, nb_genre=10, filename='scatterplot.html'):
    """
    Plot the either in 2D or in 3d
    
    Params:
        infos: for each song contains information about the song a dict {'song_name':'', 'artist_name':'', id:''}
    """
    #colors = matplotlib.cm.rainbow(np.linspace(0, 1, 10))
    c= ['hsl('+str(h)+',50%'+',50%)' for h in np.linspace(0, 360, nb_genre)]
    def get_marker(genre):
        #print(colors[g])
        return dict(
                size= 1.5,
                line={'color': 'rgb(5,65,65)', 'width': 0.01},
                color=genre,
                colorscale='Portland',
                opacity=0.8)
    def get_3D_trace(data, info, url, genre):
        return go.Scatter3d(
            x=data[:,0],
            y=data[:,1],
            z=data[:,2],
            mode='markers',
            hoverinfo='text+name',
            marker= get_marker(genre),
            customdata=url,
            name=topic2genre[genre],
            text=info)
    def get_2D_trace(data, info, url, genre):
        return go.Scatter(
            x=data[:,0],
            y=data[:,1],
            mode='markers',
            hoverinfo='text+name',
            customdata=url,
            marker= get_marker(genre),
            name=topic2genre[genre],
            text=info)
    
    traces = []
    for i in range(nb_genre):
        sel_data = data[genre == i]
        sel_info = infos[genre == i]
        sel_url = urls[genre == i]
        if sel_data.shape[1] == 3:
            traces.append(get_3D_trace(sel_data, sel_info, sel_url, i))
        else:
            traces.append(get_2D_trace(sel_data, sel_info, sel_url, i))
    my_axis = dict(
                    showbackground=False,
                    zeroline=False,
                    ticks=False,
                    showgrid=False,
                    showspikes=False,
                    showticklabels=False,
                    showtickprefix=False,
                    showexponent=False
                )
    layout = go.Layout(
            paper_bgcolor='rgb(5,65,65)',
            #plot_bgcolor='rgb(5,65,65)',
            legend=dict(
                xanchor=12,
                borderwidth=2,
                font=dict(
                    family='sans-serif',
                    size=12,
                    color='rgb(215,215,215)'
                )),
            autosize= True,
            scene=go.Scene(dict(
                xaxis=my_axis,
                yaxis=my_axis,
                zaxis=my_axis
            ))
      
    )
    return dict( data=traces, layout=layout )

def plot(data, genre, infos=None, urls=None, nb_genre=10, filename='scatterplot.html'):
    fig = go.Figure(scatter_plot(data, genre, infos, urls, nb_genre, filename))
    return plotly.offline.plot(fig, filename=filename)#, output_type='div', show_link=False, include_plotlyjs=False)

def plot2div(data, genre, infos=None, urls=None, nb_genre=10, filename='output.div'):
    fig = go.Figure(scatter_plot(data, genre, infos, urls, nb_genre, filename))
    div = plotly.offline.plot(fig, filename=filename, output_type='div', show_link=False, include_plotlyjs=False)
    text_file = open(filename, "w")
    text_file.write(div)
    text_file.close()

def build_info(row):
    return "Artist name : " + row['artist_name'] + "<br>" + \
            "Title : " + row['title'] + "<br>"+ \
            "Year : " + str(row['year'])


def plot2d_matplotlib(data, colors):
    plt.figure(figsize=(15,15))
    plt.scatter(data[:,0],data[:,1], color=colors)