
#!/usr/bin/python3
"""A simple Flask app with a single route."""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False, methods=['GET'])
def hello_hbnb():
    """Return a string at the root URL."""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False, methods=['GET'])
def hbnb():
    """Return a string at the /hbnb URL."""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False, methods=['GET'])
def c_is_fun(text):
    """Return a string at the /c/<text> URL."""
    return 'C %s' % text.replace("_", " ")


@app.route('/python/',
           defaults={'text': 'is cool'},
           strict_slashes=False, methods=['GET'])
@app.route('/python/<text>', strict_slashes=False, methods=['GET'])
def python_is_cool(text):
    """Return a string at the /python/<text> URL."""
    return 'Python %s' % text.replace("_", " ")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
