# Music Style Analysis

Follow this [link](https://cgallay.github.io/Ada) for the data story !
# Abstract

Tastes in music can be miscellaneous and very personal. Therefore, discovering enjoyable music can sometimes be very difficult and time consuming as we often don't really know what we like so much in a particular song. This project aims to help people to enrich their musical culture in an interactive way by suggesting songs that are similar with the help of a content analysis.

# Summary

The initial goal of this project was to discover how new styles of music emerge in society with respect to location, rapidity of trend propagation or also consistency in time of a style's popularity. Furthermore, we wanted to explore the influence of a hit/artist on other artists/styles.
For this purpose, we decided to work with the well-known dataset from the Labrosa website called the [Million Song Dataset](https://labrosa.ee.columbia.edu/millionsong/).

 After some investigation, we diverged from our initial idea by taking a more interactive approach for the user experience and decided to divide our project into two parts:

- The first section will consist in data analysis where we explore the features and their distribution. We present the data with some nice visualizations interaction with chronological plots and maps. Furthermore, the tracks contain a lot of useful information that allows us to determine the genre to which each track belongs the best, by making use of the artist terms feature.

- The second section will focus on the timbre feature analysis and compute the similarity between tracks using some machine learning techniques. The visualization part consists in an interactive 3D plot, where the user can walk through a data cloud, exploring the different genre of music and discover the similar tracks which are close to each other in the graph. Listening to short previews  highlights the immersive experience.

# Data enhancing

- We completed the dataset with some new features like countries by making use of the coordinate feature.
- We added a genre topic obtained with a principal component analysis of the artist terms by including the weights.
- We also added a preview link to each track in order to listen to a song sample.


# Dataset
- The [Million Song Dataset](https://labrosa.ee.columbia.edu/millionsong/)

# External music API
- [Deezer](https://developers.deezer.com/api/explorer)
- [Spotify](https://developer.spotify.com/web-api/)
