from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/lectures')
def lectures():
    return render_template('lectures.html')

@app.route('/tests')
def tests():
    return render_template('tests.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

if __name__ == '__main__':
    app.run(debug=True)