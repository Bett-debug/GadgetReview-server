import React, { useEffect, useState, useContext } from "react";
import { useParams, useNavigate } from "react-router-dom";
import ReviewForm from "../forms/ReviewForm";
import ReviewCard from "../components/ReviewCard";
import { AuthContext } from "../context/AuthContext";

const API_URL = "http://localhost:5000";

function fetchDeviceById(id) {
  return fetch(`${API_URL}/api/devices/${id}`).then((res) => {
    if (!res.ok) throw new Error("Failed to fetch device");
    return res.json();
  });
}

function fetchReviewsForDevice(deviceId) {
  return fetch(`${API_URL}/api/reviews?deviceId=${deviceId}`).then((res) => {
    if (!res.ok) throw new Error("Failed to fetch reviews");
    return res.json();
  });
}

export default function DeviceDetailPage() {
  const { id } = useParams();
  const navigate = useNavigate();
  const { token, user } = useContext(AuthContext);

  const [device, setDevice] = useState(null);
  const [reviews, setReviews] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    let mounted = true;

    fetchDeviceById(id)
      .then((dev) => {
        if (mounted) setDevice(dev);
        return fetchReviewsForDevice(id);
      })
      .then((revs) => {
        if (mounted) setReviews(revs || []);
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
    if (!token) {
      alert("You must be logged in to delete a review.");
      return;
    }

    if (window.confirm("Delete this review?")) {
      fetch(`${API_URL}/api/reviews/${reviewId}`, {
        method: "DELETE",
        headers: {
          Authorization: `Bearer ${token}`,
        },
      })
        .then((res) => {
          if (!res.ok) throw new Error("Failed to delete review");
          return res.json();
        })
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
                // show delete only if the logged-in user owns this review
                onDelete={
                  user && r.user_id === user.id
                    ? () => handleDeleteReview(r.id)
                    : null
                }
              />
            ))
          )}
        </div>
        {user ? (
          <>
            <h4>Add a review</h4>
            <ReviewForm deviceId={Number(id)} onAdded={onReviewAdded} />
          </>
        ) : (
          <p className="muted">Log in to add a review.</p>
        )}
      </section>
    </div>
  );
}
