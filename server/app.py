from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from config import Config
from models import db
from routes.device_routes import device_bp
from routes.review_routes import review_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    Migrate(app, db)
    CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}}) 

    # register blueprints
    app.register_blueprint(device_bp)
    app.register_blueprint(review_bp)

    @app.route("/")
    def home():
        return {"message": "GadgetReview API running"}

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
