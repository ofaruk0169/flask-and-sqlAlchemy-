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

@app.route('/unused_ratings')
def unused_ratings():
    five_star = 0
    four_star = 0
    three_star = 0
    two_star = 0
    one_star = 0
    output_string = '';
    movie_list = Movie.query.all()
    
    for movie in movie_list:
        if movie.rating == 1:
            one_star = one_star + 1;
        if movie.rating == 2:
            two_star = two_star + 1;
        if movie.rating == 3:
            three_star = three_star + 1;
        if movie.rating == 4:
            four_star = four_star + 1;
        if movie.rating == 5:
            five_star = five_star + 1;
    if one_star == 0:
        output_string = output_string + 'There are no 1 star movies' ;
    if two_star == 0:
        output_string = output_string + 'There are no 2 star movies' ;
    if three_star == 0:
        output_string = output_string + 'There are no 3 star movies' ;
    if four_star == 0:
        output_string = output_string + 'There are no 4 star movies' ;
    if five_star == 0:
        output_string = output_string + 'There are no 5 star movies' ;
        
    return jsonify(output_string)


