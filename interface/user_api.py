from flask import jsonify, request, app

from domain.user import User


@app.route("/api/v1/user", methods=["POST"])
def create_user():
    user = User(**request.json)
    user.create()
    return jsonify(user.to_dict()), 201


@app.route("/api/v1/user/<user_id>", methods=["GET"])
def get_user(user_id):
    user = User.get(user_id)
    return jsonify(user.to_dict()), 200
