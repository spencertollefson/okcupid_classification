from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('bootstrap.html')

@app.route('/count', methods=['POST'])
def count_words():
    text = request.form['text']
    print(text)
    count = len(text.split())
    return render_template('bootstrap.html', text=text, count=count)

if __name__ == '__main__':
    app.run(debug=True)
