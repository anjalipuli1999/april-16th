from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Welcome you all to Python Flask World v3.0 from cicd -12346785'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

