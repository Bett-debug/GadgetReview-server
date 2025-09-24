import React from "react";
import AddDeviceForm from "../forms/AddDeviceForm";

export default function AddDevicePage() {
  return (
    <div className="add-device-page">
      <h2>Suggest a New Device</h2>
      <p>
        Fill the form to suggest a new device.
      </p>
      <AddDeviceForm />
    </div>
  );
}
