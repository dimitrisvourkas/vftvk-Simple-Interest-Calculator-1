from flask import Flask, request, render_template,jsonify

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5555',debug=True)