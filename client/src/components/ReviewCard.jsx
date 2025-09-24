import React from "react";
import { Trash2 } from "lucide-react";
import RatingStars from "./RatingStars";

export default function ReviewCard({ review, onDelete }) {
  return (
    <div className="review-card">
      <div className="review-head">
        <strong>User {review.user_id}</strong>
        <div className="review-rating">
          <RatingStars rating={review.rating} />
          <span className="rating-num">{review.rating}</span>
        </div>
      </div>
      <p className="review-body">{review.comment}</p>
      <small className="review-date">
        {new Date(review.created_at).toLocaleString()}
      </small>
      {onDelete && (
        <button
          className="review-btn"
          onClick={onDelete}
        >
          <Trash2 size={15}/>
          Delete
        </button>
      )}
    </div>
  );
}
