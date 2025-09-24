import React, { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import ReviewForm from "../forms/ReviewForm";
import ReviewCard from "../components/ReviewCard";

const API_URL = "http://localhost:3001";

function fetchDeviceById(id) {
  return fetch(`${API_URL}/devices/${id}`).then((res) => {
    if (!res.ok) throw new Error("Failed to fetch device");
    return res.json();
  });
}

function fetchReviewsForDevice(deviceId) {
  return fetch(`${API_URL}/reviews?deviceId=${deviceId}`).then((res) => {
    if (!res.ok) throw new Error("Failed to fetch reviews");
    return res.json();
  });
}

function deleteReview(id) {
  return fetch(`${API_URL}/reviews/${id}`, {
    method: "DELETE",
  }).then((res) => {
    if (!res.ok) throw new Error("Failed to delete review");
    return res.json();
  });
}

export default function DeviceDetailPage() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [device, setDevice] = useState(null);
  const [reviews, setReviews] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    let mounted = true;
    Promise.all([fetchDeviceById(id), fetchReviewsForDevice(id)])
      .then(([dev, revs]) => {
        if (mounted) {
          setDevice(dev);
          setReviews(revs || []);
        }
      })
      .catch(console.error)
      .finally(() => {
        if (mounted) setLoading(false);
      });
    return () => {
      mounted = false;
    };
  }, [id]);

  function onReviewAdded(newReview) {
    setReviews((prev) => [...prev, newReview]);
  }

  function handleDeleteReview(reviewId) {
    if (window.confirm("Delete this review?")) {
      deleteReview(reviewId)
        .then(() => setReviews((prev) => prev.filter((r) => r.id !== reviewId)))
        .catch((err) => alert("Failed to delete: " + err.message));
    }
  }

  if (loading) return <p>Loading...</p>;
  if (!device) return <p>Device not found.</p>;

  return (
    <div className="detail-page">
      <button
        className="btn"
        style={{ marginBottom: "1rem" }}
        onClick={() => navigate("/devices")}
      >
        Back to Devices
      </button>
      <div className="detail-top">
        <div className="detail-image">
          <img
            src={device.image_url || "/placeholder-device.png"}
            alt={device.name}
          />
        </div>
        <div className="detail-info">
          <h2>{device.name}</h2>
          <p className="muted">
            {device.brand} • {device.category}
          </p>
          <p className="price">Ksh {device.avg_price}</p>
          <p className="specs">{device.specs}</p>
          <p>
            Recommended store:{" "}
            {device.recommended_store ? (
              <a
                href={device.recommended_store}
                target="_blank"
                rel="noreferrer"
              >
                Buy here
              </a>
            ) : (
              "—"
            )}
          </p>
        </div>
      </div>
      <section className="reviews-section">
        <h3>Reviews ({reviews.length})</h3>
        <div className="reviews-list">
          {reviews.length === 0 ? (
            <p>No reviews yet — be the first to review.</p>
          ) : (
            reviews.map((r) => (
              <ReviewCard
                key={r.id}
                review={r}
                onDelete={() => handleDeleteReview(r.id)}
              />
            ))
          )}
        </div>
        <h4>Add a review</h4>
        <ReviewForm deviceId={Number(id)} onAdded={onReviewAdded} />
      </section>
    </div>
  );
}
