from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object('config.BaseConfig')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    print(app.config)
    app.run(debug=True)
