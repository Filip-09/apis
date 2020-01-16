from flask import (
    Flask,
    render_template,
	jsonify,
	request
)

# Just a test data for now
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

# Create the application instance
app = Flask(__name__, template_folder="templates")

# Create a URL route in our application for "/"
@app.route('/', methods=['GET'])
def home():
    """
    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')
	
# A route to return all of the available entries in our catalog
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

@app.route("/api/<arg1>/<arg2>/<arg3>", methods=["GET"])
def halo(arg1,arg2,arg3):
    return user_schema.jsonify(arg2)

@app.route("/api2", methods=["GET"])
def halo2():
    arg1= request.args.get("arg1")
    arg2= request.args.get("arg2")
    arg3= request.args.get("arg3")
    return user_schema.jsonify(arg2)

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)