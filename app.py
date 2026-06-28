from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    logged = True
    food = "pizza"
    fruit = "mango"
    return render_template('home.html', foods = food, fruits = fruit, loggedin = logged)
@app.route('/about')
def about():
    username = "aideibama"
    booklist = ["atomic habit","deep work", "the alchemist"]
    return render_template('about.html', username=username, book = booklist)
if __name__ == '__main__':
    app.run(debug=True)