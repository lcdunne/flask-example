from flask import Flask

app = Flask(__name__)
app.config.from_object('config.BaseConfig')


@app.route('/')
def index():
    print(app.config)
    return "index page"


if __name__ == '__main__':
    app.run(debug=True)
