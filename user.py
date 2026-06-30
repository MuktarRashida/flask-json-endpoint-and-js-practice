from flask import Blueprint, render_template, request, jsonify
user_bp = Blueprint('user', __name__)
@user_bp.route('/api/user')
def users():
    user = {'name':'rashidat',
            'role':'developer',
            'improvement':'yes'}
    return jsonify(user)
