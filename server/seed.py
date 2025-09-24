from app import create_app, db
from models import Device

app = create_app()

def seed_data():
    with app.app_context():
        print("Seeding database...")

        # Clear existing data
        Device.query.delete()

        # Example devices
        devices = [
            Device(
                name="iPhone 15 Pro",
                brand="Apple",
                category="Smartphone",
                avg_price=1199,
                image_url="https://images.unsplash.com/photo-1697284959152-32ef13855932?w=500&auto=format&fit=crop&q=60",
                recommended_store="https://apple.com/iphone-15-pro",
                specs="A17 Pro chip, Titanium frame, 6.1-inch OLED",
                status="approved"
            ),
            Device(
                name="Samsung Galaxy S24",
                brand="Samsung",
                category="Smartphone",
                avg_price=1099,
                image_url="https://images.unsplash.com/photo-1705530292519-ec81f2ace70d?w=500&auto=format&fit=fit=crop&q=60",
                recommended_store="https://samsung.com/galaxy-s24",
                specs="Snapdragon 8 Gen 3, Dynamic AMOLED 6.8-inch",
                status="approved"
            ),
            Device(
                name="MacBook Air M3",
                brand="Apple",
                category="Laptop",
                avg_price=1499,
                image_url="https://images.unsplash.com/photo-1710905018864-d585574d79f8?w=500&auto=format&fit=crop&q=60",
                recommended_store="https://apple.com/macbook-air-m3",
                specs="M3 chip, 13-inch Retina Display, 8GB RAM",
                status="pending"
            ),
            Device(
                name="Dell XPS 13",
                brand="Dell",
                category="Laptop",
                avg_price=1299,
                image_url="https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=500&auto=format&fit=crop&q=60",
                recommended_store="https://dell.com/xps-13",
                specs="Intel i7, 13.4-inch FHD+, 16GB RAM",
                status="approved"
            ),
            Device(
                name="iPad Pro 12.9",
                brand="Apple",
                category="Tablet",
                avg_price=1099,
                image_url="https://images.unsplash.com/photo-1612831455544-3f5e8e2f1b6c?w=500&auto=format&fit=crop&q=60",
                recommended_store="https://apple.com/ipad-pro-12-9",
                specs="M2 chip, 12.9-inch Liquid Retina XDR, 128GB",
                status="approved"
            ),
            Device(
                name="Samsung Galaxy Tab S9",
                brand="Samsung",
                category="Tablet",
                avg_price=899,
                image_url="https://images.unsplash.com/photo-1612832025544-4f5e8e2f1b6d?w=500&auto=format&fit=crop&q=60",
                recommended_store="https://samsung.com/galaxy-tab-s9",
                specs="Snapdragon 8 Gen 2, 11-inch LTPS LCD, 128GB",
                status="pending"
            )
        ]

        db.session.bulk_save_objects(devices)
        db.session.commit()

        print("Database seeded!")

if __name__ == "__main__":
    seed_data()
