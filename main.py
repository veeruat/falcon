from flask import Flask, jsonify, render_template

app = Flask(__name__)

stores = [
    {
        'name': 'My name is Jesus'
    }
]


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/store')
def get_store():
    return jsonify({'store': stores})


app.run(port=5000)
