

import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "Hello World"


books = [
    {
        'id': 0,
        'title': "Fire Upon the Deep",
        'author': 'Vernor Verge',
        'first_sentence': "The coldsleep itself was dreamless",
        'year_published': "1992"
    },
    {
        'id': 1,
        'title': "The ones who walk away from Omelas",
        'author': "Ursula K. Le Guin",
        'first_sentence': 'With the clamour of bells that set the swallows \
            soaring, the Festival of Summer came to the city Omelas, \
            bright-towered toward the sea.',
        'year_published': "1975"
    },
    {
        'id': 2,
        'title': "Dhalgren",
        'author': 'Samuel R. Delany',
        'first_sentence': "to wound the autumnal city",
        'year_published': "1992"
    }
]


@app.route('/api/books', methods=["GET"])
def get_book():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error. No ID provided"

    results = []

    for book in books:
        if book['id'] == id:
            results.append(book)

    return jsonify(results)


@app.errorhandler(404)
def pagenotfound():
    return "404 - The resource code not be found.", 404


@app.route('/api/books/all', methods=["GET"])
def api_all():
    return jsonify(books)


app.run()
