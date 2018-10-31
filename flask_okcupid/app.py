from flask import Flask, jsonify, render_template, request
from api import *

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')





if __name__ == '__main__':
    app.run(debug=True)