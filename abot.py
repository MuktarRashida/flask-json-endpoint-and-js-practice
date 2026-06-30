from flask import Blueprint, render_template, request, jsonify
abot_bp = Blueprint('abot', __name__)
@abot_bp.route('/about')
def about():
    username = "aideibama"
    booklist = ["atomic habit","deep work", "the alchemist"]
    return render_template('about.html', username=username, book = booklist)
