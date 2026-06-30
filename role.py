from flask import Blueprint, render_template, request, jsonify
role_bp = Blueprint('role', __name__)
@role_bp.route('/api/role')
def text():
    name = request.args.get('names')
    return jsonify({'result': 'searched for ' + name})
