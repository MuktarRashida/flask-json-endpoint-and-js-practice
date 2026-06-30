from flask import Blueprint, render_template, request, jsonify
hom_bp = Blueprint('home', __name__)
@hom_bp.route('/')
def home():
    logged = True
    food = "pizza"
    fruit = "mango"
    return render_template('home.html', foods = food, fruits = fruit, loggedin = logged)
