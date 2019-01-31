import flask
app = flask.Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/error400')
def error400():
    flask.abort(400)


@app.route('/error500')
def error500():
    flask.abort(500)


@app.route('/stacktrace')
def stacktrace():
    raise ValueError('Stacktrace')


def main():
    index()


if __name__ == '__main__':
    main()
