from flask import Blueprint, request, jsonify
from models import db, Review
from datetime import datetime
from flask_jwt_extended import jwt_required, get_jwt_identity

review_bp = Blueprint("reviews", __name__, url_prefix="/api/reviews")



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
    return jsonify([r.to_dict() for r in reviews])



@review_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_review(id):
    user_id = int(get_jwt_identity())  
    review = Review.query.get_or_404(id)

    if review.user_id != user_id:
        return jsonify({"error": "Not authorized to delete this review"}), 403

    db.session.delete(review)
    db.session.commit()
    return jsonify({"message": "Review deleted"}), 200



@review_bp.route("", methods=["POST"])
@jwt_required()
def add_review():
    user_id = int(get_jwt_identity())  
    data = request.get_json()

    try:
        new_review = Review(
            deviceId=int(data["deviceId"]),
            user_id=user_id,
            rating=int(data["rating"]), 
            comment=data.get("comment", ""),
            created_at=datetime.utcnow(),
        )
        db.session.add(new_review)
        db.session.commit()
        return jsonify(new_review.to_dict()), 201
    except (ValueError, TypeError, KeyError):
        return jsonify({"error": "Failed to add review. Check data."}), 400
