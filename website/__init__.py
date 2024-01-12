from flask import Flask, render_template, request
from flask import Flask
from flask import jsonify
from flask import request

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "sekretnehaslo"
jwt = JWTManager(app)


@app.route("/")
def index():
    return render_template("index.html")
    # return "<h1>Hello world!</h1>"


@app.route("/login", methods=['GET', 'POST'])
def login():
    username = request.form.get("username", None)
    password = request.form.get("password", None)
    if username != "test" or password != "test":
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)


# @app.route("/protected", methods=["GET"])
# @jwt_required()
# def protected():
#     # Access the identity of the current user with get_jwt_identity
#     current_user = get_jwt_identity()
#     return jsonify(logged_in_as=current_user), 200


# @app.route("/summoner", methods=["POST"])
# def summoner():
#     return render_template("summoner.html")



if __name__ == '__main__':
    app.run(port=80)
