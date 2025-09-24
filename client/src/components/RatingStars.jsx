import { Star } from "lucide-react";

export default function RatingStars({ rating = 0 }) {
  const fullStars = Math.floor(rating);

  return (
    <span className="rating-stars">
      {Array.from({ length: fullStars }).map((_, i) => (
        <Star key={`full-${i}`} fill="#fbbf24" strokeWidth={0} />
      ))}
    </span>
  );
}
