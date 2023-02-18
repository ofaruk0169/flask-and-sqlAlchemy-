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
        if movie.title[0] == ‘A’:
            movies.append({'id' : movie.id, 'title' : movie.title, 'rating' : movie.rating})
    return jsonify({'movies': movies})