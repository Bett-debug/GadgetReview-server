import React from "react";
import AddDeviceForm from "../forms/AddDeviceForm";

export default function AddDevicePage() {
  return (
    <div>
      <h2>Suggest a New Device</h2>
      <p>
        Fill the form to suggest a new device. Suggestions will be reviewed by
        admin.
      </p>
      <AddDeviceForm />
    </div>
  );
}
