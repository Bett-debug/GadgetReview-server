from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import Config
from models import db, bcrypt
from routes.device_routes import device_bp
from routes.review_routes import review_bp
from routes.auth_routes import auth_bp   

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    Migrate(app, db)
    CORS(app, origins="http://localhost:3000")  # allow React frontend

    # register blueprints
    app.register_blueprint(device_bp)
    app.register_blueprint(review_bp)
    app.register_blueprint(auth_bp)

    @app.route("/")
    def home():
        return {"message": "GadgetReview API running"}

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
