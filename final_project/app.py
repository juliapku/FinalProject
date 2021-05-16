from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/gallery')
def gallery():
    return render_template('margielagallery.html')

@app.route('/margiela')
def margiela():
    return render_template('margiela.html')

if __name__ == '__main__':
    app.run(debug=True)