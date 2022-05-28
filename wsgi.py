import json
import os

import flask
from flask import Flask, request, jsonify

import util

app = Flask(__name__)

model, mat_movies = util.pre_process()


@app.route("/")
def welcome():
    return flask.render_template('welcome.html')


@app.route("/movie/<movie>")
def recommend_movie(movie):
    args = request.args
    output = util.recommender(movie, mat_movies, model, args.get('count', default=10, type=int))
    return jsonify(success=True, message="Data Retrieved Successfully.", data=output), 201


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port, debug=True)

