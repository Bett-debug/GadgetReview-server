import { Star, StarHalf } from "lucide-react";

export default function RatingStars({ rating = 0 }) {
  const fullStars = Math.floor(rating);
  const hasHalf = rating - fullStars >= 0.5;
  const emptyStars = 5 - fullStars - (hasHalf ? 1 : 0);

  return (
    <span className="rating-stars">
      {Array.from({ length: fullStars }).map((_, i) => (
        <Star key={`full-${i}`} fill="#fbbf24" strokeWidth={0} />
      ))}
    </span>
  );
}
