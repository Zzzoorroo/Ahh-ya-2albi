from flask import Flask
from routes.auth_routes import auth_bp
from routes.dashboard_routes import dashboard_bp
from routes.api_routes import api_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    #Initialize the database
    db.init_app(app)

    #Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(api_bp)

    return app


if __name__ == "__main__":
    app= create_app()
    app.run(debug=True)
