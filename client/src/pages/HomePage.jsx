import React from "react";
import { Link } from "react-router-dom";
import { Smartphone, Star, Funnel } from "lucide-react";

function HomePage() {
  return (
    <div className="container">
      <div className="page-header">
        <h1>Welcome to GadgetReview</h1>
        <p>
          Discover devices, explore specifications, compare prices, and share
          reviews all in one place.
        </p>
      </div>

      <div className="card">
        <h2>Your one-stop gadget discovery platform</h2>
        <p>
          We help you find the best phones, laptops, and tablets with detailed
          specs, reviews, and store recommendations.
        </p>
        <div>
          <Link to="/devices" className="btn primary">
            Browse Devices
          </Link>
          <Link to="/add-device" className="btn card-btn">
            Add a Device
          </Link>
        </div>
      </div>

      <div className="grid">
        <div className="card">
          <h3>
            <Smartphone color="#6366f1" />
            Device Catalog
          </h3>
          <p>
            Browse phones, laptops, tablets, and more. View detailed
            specifications and average market prices.
          </p>
        </div>
        <div className="card">
          <h3>
            <Star color="#6366f1" />
            Independent Reviews
          </h3>
          <p>
            Read and share honest reviews from other users to make smarter
            buying decisions.
          </p>
        </div>
        <div className="card">
          <h3>
            <Funnel color="#6366f1" />
            Smart Filtering
          </h3>
          <p>
            Use filters to find the perfect device match based on your budget
            and preferences.
          </p>
        </div>
      </div>

      <div className="card-bottom">
        <h2>Ready to find your next gadget?</h2>
        <p>Start browsing or add your own device to help others!</p>
        <Link to="/devices" className="btn primary">
          Get Started
        </Link>
      </div>
    </div>
  );
}

export default HomePage;
