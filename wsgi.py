import json
import os

from flask import Flask, request, jsonify

import util

app = Flask(__name__)

model, mat_movies = util.pre_process()


@app.route("/")
def welcome():
    return """Hello, Welcome to movie recommender api.
    Please browse https://movie-recommander.herokuapp.com/movie/<movie_name>?count=<no_of_suggested_movies> link to get suggested movies."""

@app.route("/movie/<movie>")
def recommend_movie(movie):
    args = request.args
    output = util.recommender(movie, mat_movies, model, args.get('count', default=10, type=int))
    return jsonify(success=True, message="Data Retrieved Successfully.", data=output), 201


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

