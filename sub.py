from flask import Blueprint, render_template, request, jsonify
sub_bp = Blueprint('sub', __name__)
@sub_bp.route('/submit', methods = ['GET','POST'])
def submit():
    if request.method == 'POST':
        response = request.form.get('username')
        return render_template('home.html', display = response)
    return render_template('form.html')
