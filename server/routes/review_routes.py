from flask import Blueprint, request, jsonify
from models import db, Review

review_bp = Blueprint("reviews", __name__, url_prefix="/api/reviews")

@review_bp.route("", methods=["GET"])
def get_reviews():
    device_id = request.args.get("deviceId")
    query = Review.query
    if device_id:
        query = query.filter_by(device_id=device_id)
    reviews = query.all()
    return jsonify([r.to_dict() for r in reviews])

@review_bp.route("", methods=["POST"])
def add_review():
    data = request.get_json()
    new_review = Review(
        device_id=data["deviceId"],
        user_id=data["user_id"],
        rating=data["rating"],
        comment=data.get("comment", "")
    )
    db.session.add(new_review)
    db.session.commit()
    return jsonify(new_review.to_dict()), 201
