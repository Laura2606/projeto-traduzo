from bson import ObjectId
from flask import Blueprint, jsonify, request
from models.history_model import HistoryModel
from models.user_model import UserModel

admin_controller = Blueprint("admin_controller", __name__)


@admin_controller.route("/history/<id>", methods=["DELETE"])
def history_delete(id):
    admin_token = request.headers["Authorization"]
    admin_username = request.headers["User"]

    user = UserModel.find_one({"name": admin_username})

    if not user or not user.token_is_valid(admin_token):
        return jsonify({"error": "Unauthorized Access"}), 401

    history = HistoryModel.find_one({"_id": ObjectId(id)})
    if not history:
        return jsonify({"error": "History not found"}), 404
    else:
        history.delete()
        return "", 204
