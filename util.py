import pickle

import pandas as pd
from fuzzywuzzy import process

movies = pd.read_csv('./resources/movies.csv')


def pre_process():
    model_pickle_file = open('./resources/example_pickle', 'rb')
    model = pickle.load(model_pickle_file)
    model_pickle_file.close()

    mat_movies_pickle = open('./resources/mat_movie_pickle', 'rb')
    mat_movies = pickle.load(mat_movies_pickle)
    mat_movies_pickle.close()
    return model, mat_movies


def recommender(movie_name, data, model, n):
    res = process.extractOne(movie_name, movies['title'])
    print(res)
    idx = res[2]
    print('Movie Selected : ', movies['title'][idx], 'Index: ', idx)
    print('Searching for recommendation.....')
    distance, indices = model.kneighbors(data[idx], n_neighbors=n)
    output = []
    movies['title'].dropna()
    for i in indices[0]:
        output.append(str((movies['title'][i])))
    return output
