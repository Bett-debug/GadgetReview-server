from app import create_app, db
from models import Device, Review

app = create_app()

def seed_data():
    with app.app_context():
        print("Seeding database...")

        Review.query.delete()
        Device.query.delete()

        # Devices data
        devices_data = [
            {
                "id": "1",
                "name": "iPhone 15 Pro",
                "brand": "Apple",
                "category": "Smartphone",
                "avg_price": 60999,
                "specs": "A17 Bionic, 6.1-inch OLED, Triple Camera",
                "image_url": "https://images.unsplash.com/photo-1697284959152-32ef13855932?w=500&auto=format&fit=crop&q=60",
                "recommended_store": "https://apple.com/iphone-15-pro",
            },
            {
                "id": "2",
                "name": "Samsung Galaxy S24",
                "brand": "Samsung",
                "category": "Smartphone",
                "avg_price": 80909,
                "specs": "Snapdragon 8 Gen 3, 6.5-inch AMOLED, Quad Camera",
                "image_url": "https://images.unsplash.com/photo-1705530292519-ec81f2ace70d?w=500&auto=format&fit=crop&q=60",
                "recommended_store": "https://samsung.com/galaxy-s24",
            },
            {
                "id": "3",
                "name": "MacBook Air M3",
                "brand": "Apple",
                "category": "Laptop",
                "avg_price": 12990,
                "specs": "M3 Chip, 13-inch Retina, 18h Battery Life",
                "image_url": "https://images.unsplash.com/photo-1710905018864-d585574d79f8?w=500&auto=format&fit=crop&q=60",
                "recommended_store": "https://www.apple.com/ke/macbook-air/",
            },
            {
                "id": "4",
                "name": "Dell XPS 15",
                "brand": "Dell",
                "category": "Laptop",
                "avg_price": 15990,
                "specs": "Intel Core i7, 15.6-inch OLED, NVIDIA RTX 4050",
                "image_url": "https://images.unsplash.com/photo-1593642632823-8f785ba67e45?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8RGVsbCUyMFhQUyUyMDE1fGVufDB8fDB8fHww",
                "recommended_store": "https://www.dell.com/en-us/shop/dell-laptops/xps-15-laptop/spd/xps-15-9530-laptop",
            },
            {
                "id": "5",
                "name": "iPad Pro M4",
                "brand": "Apple",
                "category": "Tablet",
                "avg_price": 10990,
                "specs": "M4 Chip, 11-inch Liquid Retina, ProMotion",
                "image_url": "https://images.unsplash.com/photo-1691599703441-58bee2410f42?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjB8fGlQYWQlMjBQcm8lMjBNNHxlbnwwfHwwfHx8MA%3D%3D",
                "recommended_store": "https://apple.com/ipad-pro",
            },
            {
                "id": "6",
                "name": "Samsung Galaxy Tab S9",
                "brand": "Samsung",
                "category": "Tablet",
                "avg_price": 79900,
                "specs": "Snapdragon 8 Gen 2, 11-inch Dynamic AMOLED 2X",
                "image_url": "https://images.unsplash.com/flagged/photo-1557050406-b3d281ecde9b?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8U2Ftc3VuZyUyMEdhbGF4eSUyMHRhYmxldHxlbnwwfHwwfHx8MA%3D%3D",
                "recommended_store": "https://www.phoneplacekenya.com/product/samsung-galaxy-tab-s9/?srsltid=AfmBOopo2oOr575F27CbS-Ce-4bWwWNS4fQrG8MWhniHYBa9ACKKcGcC",
            },
            {
                "id": "7",
                "name": "Google Pixel 8",
                "brand": "Google",
                "category": "Smartphone",
                "avg_price": 69900,
                "specs": "Tensor G3, 6.2-inch OLED, Dual Camera",
                "image_url": "https://images.unsplash.com/photo-1697355360151-2866de32ad4d?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8R29vZ2xlJTIwUGl4ZWwlMjA4fGVufDB8fDB8fHww",
                "recommended_store": "https://store.google.com/product/pixel_8",
            },
            {
                "id": "8",
                "name": "Lenovo Yoga 7i",
                "brand": "Lenovo",
                "category": "Laptop",
                "avg_price": 85000,
                "specs": "Intel Core i5, 14-inch Touchscreen, 2-in-1",
                "image_url": "https://images.unsplash.com/photo-1611078489935-0cb964de46d6?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8TGVub3ZvfGVufDB8fDB8fHww",
                "recommended_store": "https://www.lenovo.com/ke/en/p/laptops/yoga/yoga-2-in-1-series/yoga-7i-gen-8-(14-inch-intel)/len101y0030?srsltid=AfmBOorDwhQXikhmaYopSHV7gT2yfeGeTQSU83EOdWCwQyfEoTQvSmdU",
            },
            {
                "id": "9",
                "name": "Acer Chromebook Spin 714",
                "brand": "Acer",
                "category": "Laptop",
                "avg_price": 70000,
                "specs": "Intel Core i5, 14-inch, Chrome OS",
                "image_url": "https://images.unsplash.com/photo-1693206578601-21cdc341d2c8?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8QWNlciUyMENocm9tZWJvb2slMjBTcGluJTIwNzE0fGVufDB8fDB8fHww",
                "recommended_store": "https://acer.com/chromebook-spin-714",
            },
            {
                "id": "10",
                "name": "OnePlus 12",
                "brand": "OnePlus",
                "category": "Smartphone",
                "avg_price": 79900,
                "specs": "Snapdragon 8 Gen 3, 6.8-inch AMOLED, 100W Charging",
                "image_url": "https://images.unsplash.com/photo-1614796740292-50ae67262ff0?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8T25lUGx1c3xlbnwwfHwwfHx8MA%3D%3D",
                "recommended_store": "https://oneplus.com/oneplus-12",
            },
            {
                "id": "11",
                "name": "Microsoft Surface Pro 9",
                "brand": "Microsoft",
                "category": "Tablet",
                "avg_price": 10990,
                "specs": "Intel Core i5, 13-inch, Windows 11",
                "image_url": "https://images.unsplash.com/photo-1621570360476-a0c6945ebb79?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8TWljcm9zb2Z0JTIwU3VyZmFjZSUyMFBybyUyMDl8ZW58MHx8MHx8fDA%3D",
                "recommended_store": "https://www.microsoft.com/en-in/surface/devices/surface-pro-9",
            },
            {
                "id": "12",
                "name": "Asus ROG Ally",
                "brand": "Asus",
                "category": "Smartphone",
                "avg_price": 6990,
                "specs": "AMD Z1 Extreme, 7-inch FHD, Windows 11",
                "image_url": "https://images.unsplash.com/photo-1732020883995-79f0a0595101?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8N3x8QXN1cyUyMFJPR3xlbnwwfHwwfHx8MA%3D%3D",
                "recommended_store": "https://rog.asus.com/gaming-handhelds/rog-ally/rog-ally-2023/",
            },
            {
                "id": "13",
                "name": "HP Spectre x360",
                "brand": "HP",
                "category": "Laptop",
                "avg_price": 14000,
                "specs": "Intel Core i7, 13.5-inch OLED, 2-in-1",
                "image_url": "https://images.unsplash.com/photo-1589561084283-930aa7b1ce50?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8SFAlMjBTcGVjdHJlJTIweDM2MHxlbnwwfHwwfHx8MA%3D%3D",
                "recommended_store": "https://www.hp.com/us-en/shop/slp/spectre-family/hp-spectre-x-360",
            },
            {
                "id": "14",
                "name": "Nothing Phone (2a)",
                "brand": "Nothing",
                "category": "Smartphone",
                "avg_price": 34900,
                "specs": "MediaTek Dimensity 7200 Pro, 6.7-inch AMOLED",
                "image_url": "https://images.unsplash.com/photo-1711239682372-fd545e32cb5b?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Tm90aGluZyUyMFBob25lJTIwKDJhKXxlbnwwfHwwfHx8MA%3D%3D",
                "recommended_store": "https://www.phoneplacekenya.com/product/nothing-phone-2a/?srsltid=AfmBOorMKk8kB6Sprd5cDRI2OblaksJCRgFj7AadlPTCDt8kfd8SlNAI",
            },
            {
                "id": "15",
                "name": "Oppo Pad Air",
                "brand": "Oppo",
                "category": "Tablet",
                "avg_price": 27900,
                "specs": "Snapdragon 680, 10.36-inch, 60Hz",
                "image_url": "https://media.istockphoto.com/id/1473982713/photo/modern-technologies-for-training-tablet-with-a-stylus-on-a-blue-background-3d-render.webp?a=1&b=1&s=612x612&w=0&k=20&c=H50Tu6x75PYG6WTT9-EKqjkvy9vFP5QjIyasKmrqYe8=",
                "recommended_store": "https://www.oppo.com/en/accessories/oppo-pad-air/",
            },
            {
                "id": "16",
                "name": "Samsung Galaxy Watch6",
                "brand": "Samsung",
                "category": "Smartphone",
                "avg_price": 3000,
                "specs": "Exynos W930, 1.5-inch display",
                "image_url": "https://images.unsplash.com/photo-1623319496365-1d045be389e2?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8U2Ftc3VuZyUyMEdhbGF4eSUyMFdhdGNoNnxlbnwwfHwwfHx8MA%3D%3D",
                "recommended_store": "https://www.samsung.com/africa_en/watches/galaxy-watch/galaxy-watch6-44mm-graphite-bluetooth-sm-r940nzkamea/",
            },
            {
                "id": "17",
                "name": "Kindle Paperwhite",
                "brand": "Amazon",
                "category": "Tablet",
                "avg_price": 14000,
                "specs": "6.8-inch display, Waterproof",
                "image_url": "https://images.unsplash.com/photo-1623751370867-159020187c16?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8S2luZGxlJTIwUGFwZXJ3aGl0ZXxlbnwwfHwwfHx8MA%3D%3D",
                "recommended_store": "https://www.amazon.com/Kindle-Paperwhite-adjustable-Ad-Supported/dp/B08KTZ8249",
            },
            {
                "id": "18",
                "name": "Google Nest Hub",
                "brand": "Google",
                "category": "Tablet",
                "avg_price": 8000,
                "specs": "7-inch touchscreen, Smart home control",
                "image_url": "https://images.unsplash.com/photo-1650682009477-52fd77302b78?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8R29vZ2xlJTIwTmVzdCUyMEh1YnxlbnwwfHwwfHx8MA%3D%3D",
                "recommended_store": "https://store.google.com/product/nest_hub",
            },
        ]

        devices = [Device(**d) for d in devices_data]
        db.session.bulk_save_objects(devices)
        db.session.commit()

        print("Devices seeded!")

        reviews_data = [
        {
      "id": "1",
      "deviceId": "1",
      "user_id": 101,
      "rating": 5,
      "comment": "Amazing phone, battery lasts all day!",
      "created_at": "2024-04-10T12:00:00Z"
    },
    {
      "id": "2",
      "deviceId": "1",
      "user_id": 102,
      "rating": 4,
      "comment": "Great camera, but a bit expensive.",
      "created_at": "2024-04-11T12:00:00Z"
    },
    {
      "id": "3",
      "deviceId": "1",
      "user_id": 103,
      "rating": 5,
      "comment": "The best phone I have ever owned. The new action button is a game-changer.",
      "created_at": "2024-04-12T12:00:00Z"
    },
    {
      "id": "4",
      "deviceId": "2",
      "user_id": 201,
      "rating": 5,
      "comment": "Best Android phone I’ve used so far! The AI features are surprisingly useful.",
      "created_at": "2024-04-13T12:00:00Z"
    },
    {
      "id": "5",
      "deviceId": "2",
      "user_id": 202,
      "rating": 4,
      "comment": "The display is incredibly vibrant. Performance is top-notch.",
      "created_at": "2024-04-14T12:00:00Z"
    },
    {
      "id": "6",
      "deviceId": "3",
      "user_id": 301,
      "rating": 5,
      "comment": "The M3 chip is a marvel. This laptop is silent and extremely fast.",
      "created_at": "2024-04-15T12:00:00Z"
    },
    {
      "id": "7",
      "deviceId": "3",
      "user_id": 302,
      "rating": 3,
      "comment": "Good performance, but the design is getting old. Wish they'd updated the look.",
      "created_at": "2024-04-16T12:00:00Z"
    },
    {
      "id": "8",
      "deviceId": "4",
      "user_id": 401,
      "rating": 5,
      "comment": "This laptop is a beast for video editing! The OLED screen is beautiful.",
      "created_at": "2024-04-17T12:00:00Z"
    },
    {
      "id": "9",
      "deviceId": "5",
      "user_id": 501,
      "rating": 4,
      "comment": "Perfect for drawing and taking notes. The screen is incredible.",
      "created_at": "2024-04-18T12:00:00Z"
    },
    {
      "id": "10",
      "deviceId": "6",
      "user_id": 601,
      "rating": 4,
      "comment": "A solid tablet for the price. The screen is vibrant and the S Pen is a nice bonus.",
      "created_at": "2024-04-19T12:00:00Z"
    },
    {
      "id": "11",
      "deviceId": "7",
      "user_id": 701,
      "rating": 5,
      "comment": "The camera on this phone is unreal! The software features are fantastic.",
      "created_at": "2024-04-20T12:00:00Z"
    },
    {
      "id": "12",
      "deviceId": "8",
      "user_id": 801,
      "rating": 4,
      "comment": "Love the flexibility of the 2-in-1 design. Great for work and media.",
      "created_at": "2024-04-21T12:00:00Z"
    },
    {
      "id": "13",
      "deviceId": "9",
      "user_id": 901,
      "rating": 4,
      "comment": "Fast and reliable. Perfect for a student on a budget.",
      "created_at": "2024-04-22T12:00:00Z"
    },
    {
      "id": "14",
      "deviceId": "10",
      "user_id": 1001,
      "rating": 4,
      "comment": "Great charging speed! Battery life is decent too.",
      "created_at": "2024-04-23T12:00:00Z"
    },
    {
      "id": "15",
      "deviceId": "11",
      "user_id": 1101,
      "rating": 5,
      "comment": "The perfect tablet for a power user. Replaced my old laptop.",
      "created_at": "2024-04-24T12:00:00Z"
    },
    {
      "id": "16",
      "deviceId": "12",
      "user_id": 1201,
      "rating": 4,
      "comment": "A very capable handheld. Can't believe it runs Windows.",
      "created_at": "2024-04-25T12:00:00Z"
    },
    {
      "id": "17",
      "deviceId": "13",
      "user_id": 1301,
      "rating": 5,
      "comment": "Beautiful design and great for travel. The battery lasts all day.",
      "created_at": "2024-04-26T12:00:00Z"
    },
    {
      "id": "18",
      "deviceId": "14",
      "user_id": 1401,
      "rating": 4,
      "comment": "A unique look and smooth performance. Excellent value for the price.",
      "created_at": "2024-04-27T12:00:00Z"
    },
    {
      "id": "19",
      "deviceId": "15",
      "user_id": 1501,
      "rating": 3,
      "comment": "A basic tablet, but good enough for watching videos and light browsing.",
      "created_at": "2024-04-28T12:00:00Z"
    },
    {
      "id": "20",
      "deviceId": "16",
      "user_id": 1601,
      "rating": 4,
      "comment": "Great fitness tracking and a bright display. Looks stylish too.",
      "created_at": "2024-04-29T12:00:00Z"
    },
    {
      "id": "21",
      "deviceId": "17",
      "user_id": 1701,
      "rating": 5,
      "comment": "My go-to device for reading. It's so light and easy on the eyes.",
      "created_at": "2024-04-30T12:00:00Z"
    },
    {
      "id": "22",
      "deviceId": "18",
      "user_id": 1801,
      "rating": 4,
      "comment": "Convenient for controlling my smart home devices with voice commands.",
      "created_at": "2024-05-01T12:00:00Z"
    },
        ]

        from datetime import datetime
        for r in reviews_data:
            r["deviceId"] = r.pop("deviceId")
            r["created_at"] = datetime.fromisoformat(r["created_at"].replace("Z", "+00:00"))

        reviews = [Review(**r) for r in reviews_data]
        db.session.bulk_save_objects(reviews)
        db.session.commit()

        print("Reviews seeded!")
        print("Database seeding completed!")

if __name__ == "__main__":
    seed_data()
