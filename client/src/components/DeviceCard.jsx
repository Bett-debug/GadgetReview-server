import React from "react";
import { Link } from "react-router-dom";
import RatingStars from "./RatingStars";

export default function DeviceCard({ device }) {
  const avg = device.avg_rating ?? device.avg_price ? device.avg_rating : null;
  return (
    <article className="card device-card">
      <div className="card-media">
        {/* placeholder image */}
        <img
          src={device.image_url || "/placeholder-device.png"}
          alt={device.name}
        />
      </div>
      <div className="card-body">
        <h3 className="device-title">{device.name}</h3>
        <p className="device-sub">
          {device.brand} • {device.category}
        </p>
        <div className="card-meta">
          <div className="price">Ksh {device.avg_price ?? "—"}</div>
          <div className="rating">
            <RatingStars rating={device.avg_rating ?? 0} />
            <small className="rating-count">{device.reviews_count ?? 0}</small>
          </div>
        </div>
        <p className="short-spec">{device.short_spec || ""}</p>
        <Link to={`/devices/${device.id}`} className="card-link">
          View details
        </Link>
      </div>
    </article>
  );
}
