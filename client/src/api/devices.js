const API_URL = "http://localhost:5000/api";

export async function fetchDeviceById(id) {
  const res = await fetch(`${API_URL}/devices/${id}`);
  if (!res.ok) throw new Error("Failed to fetch device");
  return res.json();
}

// You can also add the function to fetch all devices here
export async function fetchAllDevices() {
  const res = await fetch(`${API_URL}/devices`);
  if (!res.ok) throw new Error("Failed to fetch devices");
  return res.json();
}
