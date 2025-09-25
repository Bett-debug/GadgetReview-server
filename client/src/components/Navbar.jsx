import React from "react";
import { Link } from "react-router-dom";
import {
  MonitorSmartphone,
  Plus,
  Smartphone,
  Home,
  LogIn,
  UserPlus,
} from "lucide-react";

export default function Navbar() {
  return (
    <nav className="navbar">
      <div className="nav-inner">
        <Link to="/" className="brand">
          <MonitorSmartphone />
          GadgetReview
        </Link>

        <div className="nav-links">
          <Link to="/">
            <Home />
            Home
          </Link>

          <Link to="/devices">
            <Smartphone />
            Devices
          </Link>

          <Link to="/add-device" className="btn">
            <Plus />
            Add Device
          </Link>

          <Link to="/login">
            <LogIn />
            Login
          </Link>

          <Link to="/register">
            <UserPlus />
            Register
          </Link>

          
        </div>
      </div>
    </nav>
  );
}
