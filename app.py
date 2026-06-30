from flask import Flask

app = Flask(__name__)
from hom import hom_bp
from abot import abot_bp
from role import role_bp
from user import user_bp
from sub import sub_bp

app.register_blueprint(hom_bp)
app.register_blueprint(abot_bp)
app.register_blueprint(role_bp)
app.register_blueprint(user_bp)
app.register_blueprint(sub_bp)

if __name__ == '__main__':
    app.run(debug=True)