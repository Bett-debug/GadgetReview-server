import React from "react";

export default function RatingStars({ rating = 0 }) {
  const full = Math.round(rating);
  return (
    <span className="rating-stars">
      {Array.from({ length: 5 }).map((_, i) => (
        <svg
          key={i}
          className={`star ${i < full ? "full" : ""}`}
          viewBox="0 0 24 24"
          width="16"
          height="16"
          aria-hidden
        >
          <path d="M12 .587l3.668 7.431 8.2 1.192-5.934 5.787 1.402 8.17L12 18.896 4.664 23.167l1.402-8.17L.132 9.21l8.2-1.192z" />
        </svg>
      ))}
    </span>
  );
}
