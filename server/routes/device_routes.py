from flask import Blueprint, request, jsonify
from models import db, Device

device_bp = Blueprint("devices", __name__, url_prefix="/api/devices")


@device_bp.route("", methods=["GET"])
def get_devices():
    devices = Device.query.all()
    return jsonify([d.to_dict() for d in devices])


@device_bp.route("/<int:id>", methods=["GET"])
def get_device(id):
    device = Device.query.get_or_404(id)
    return jsonify(device.to_dict())


@device_bp.route("", methods=["POST"])
def add_device():
    data = request.get_json()
    new_device = Device(
        name=data["name"],
        brand=data["brand"],
        category=data["category"],
        avg_price=data["avg_price"],
        image_url=data.get("image_url"),
        recommended_store=data.get("recommended_store"),
        specs=data.get("specs"),
        status="pending",
    )
    db.session.add(new_device)
    db.session.commit()
    return jsonify(new_device.to_dict()), 201
