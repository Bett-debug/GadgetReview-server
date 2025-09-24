const API_URL = "http://localhost:5000/api";

export async function fetchReviewsForDevice(deviceId) {
  const res = await fetch(`${API_URL}/reviews?deviceId=${deviceId}`);
  if (!res.ok) throw new Error("Failed to fetch reviews");
  return res.json();
}

export async function addReview(review) {
  const res = await fetch(`${API_URL}/reviews`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(review),
  });
  if (!res.ok) throw new Error("Failed to add review");
  return res.json();
}
