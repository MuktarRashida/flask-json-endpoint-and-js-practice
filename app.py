from flask import Flask, render_template, request, jsonify
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
@app.route('/submit', methods = ['GET','POST'])
def submit():
    if request.method == 'POST':
        response = request.form.get('username')
        return render_template('result.html', result = response)
    return render_template('form.html')
@app.route('/api/user')
def users():
    user ={'name':'aideibama',
           'role':'developer',
           'improvements':'yes'}
    return jsonify(user)
if __name__ == '__main__':
    app.run(debug=True)