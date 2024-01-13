from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask import jsonify
from flask import request

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager


# db = SQLAlchemy()
# DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config["JWT_SECRET_KEY"] = "sekretnehaslo"
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # db.init_app(app)
    # jwt = JWTManager(app)


    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # from .models import User

    return app


# def create_database(app):
#     if not path.exists('website/' + DB_NAME):
#         db.create_all(app)
#         print('Created Database')




# @app.route("/login", methods=['GET', 'POST'])
# def login():
#     username = request.form.get("username", None)
#     password = request.form.get("password", None)
#     if username != "test" or password != "test":
#         return jsonify({"msg": "Bad username or password"}), 401
#
#     access_token = create_access_token(identity=username)
#     return jsonify(access_token=access_token)
#
#
#

# if __name__ == '__main__':
#     app.run(port=80)
