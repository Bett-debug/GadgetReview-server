from flask import Blueprint, request, jsonify
from models import db, Review

review_bp = Blueprint("reviews", __name__, url_prefix="/api/reviews")


# -------------------- GET Reviews --------------------
@review_bp.route("", methods=["GET"])
def get_reviews():
    deviceId_str = request.args.get("deviceId")
    query = Review.query

    if deviceId_str:
        try:
            deviceId = int(deviceId_str)
            query = query.filter_by(deviceId=deviceId)
        except (ValueError, TypeError):
            return jsonify({"error": "Invalid deviceId format"}), 400

    reviews = query.all()
    return jsonify([r.to_dict() for r in reviews]), 200


# -------------------- POST Review --------------------
@review_bp.route("", methods=["POST"])
def add_review():
    data = request.get_json()

    # Validate required fields
    if not data or "deviceId" not in data or "user_id" not in data or "rating" not in data:
        return jsonify({"error": "deviceId, user_id, and rating are required"}), 400

    try:
        new_review = Review(
            deviceId=int(data["deviceId"]),
            user_id=int(data["user_id"]),
            rating=int(data["rating"]),
            comment=data.get("comment", ""),
        )
        db.session.add(new_review)
        db.session.commit()
        return jsonify(new_review.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Failed to add review: {str(e)}"}), 400


# -------------------- DELETE Review --------------------
@review_bp.route("/<int:id>", methods=["DELETE"])
def delete_review(id):
    review = Review.query.get_or_404(id)
    db.session.delete(review)
    db.session.commit()
    return jsonify({"message": f"Review {id} deleted"}), 200
