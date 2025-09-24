import React from "react";
import RatingStars from "./RatingStars";

export default function ReviewCard({ review }) {
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
    </div>
  );
}
