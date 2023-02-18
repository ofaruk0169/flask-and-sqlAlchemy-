import flask
from flask import jsonify
import sqlalchemy
from flaskapp import database, models
from flaskapp.database import dbSession
from flaskapp.models import Movie

app = flask.Flask(__name__)
database.initdb()

@app.route('/add_movie', methods=['POST'])
def add_movie():
    return 'Done', 201

@app.route('/movies')
def movies():
    movie_list = Movie.query.all()
    movies = []
    for movie in movie_list:
        movies.append({'id' : movie.id, 'title' : movie.title, 'rating' : movie.rating})
    return jsonify({'movies': movies})

@app.route('/sorted_movies')
def sort_movies():
    movie_list = Movie.query.all()
    movies = []
    for movie in movie_list:
        movies.append({'id' : movie.id, 'title' : movie.title, 'rating' : movie.rating})
    movies = sort(movies)
    return jsonify({'sorted_movies': movies})

def sort(movie_list):
    print('movie_list is ', movie_list);
    swap = True
    i = 0
    while swap:
        swap = False
        for i in range(len(movie_list)-1):
            next_movie = movie_list[i+1]
            if movie_list[i]['rating'] < next_movie['rating']:
                swap = True
                movie_list[i], movie_list[i+1] = movie_list[i+1], movie_list[i]
    return movie_list


