import flask
app = flask.Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


def main():
    index()


if __name__ == '__main__':
    main()
