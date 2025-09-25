from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Device(db.Model):
    __tablename__ = "devices"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    brand = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    avg_price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(255))
    recommended_store = db.Column(db.String(255))
    specs = db.Column(db.Text)
    status = db.Column(db.String(20), default="pending")

    reviews = db.relationship("Review", backref="device", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "brand": self.brand,
            "category": self.category,
            "avg_price": self.avg_price,
            "image_url": self.image_url,
            "recommended_store": self.recommended_store,
            "specs": self.specs,
            "status": self.status,
        }


class Review(db.Model):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True)
    deviceId = db.Column(
        db.Integer,
        db.ForeignKey("devices.id", name="fk_reviews_deviceId"),
        nullable=False
    )
    user_id = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "deviceId": self.deviceId,
            "user_id": self.user_id,
            "rating": self.rating,
            "comment": self.comment,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }
