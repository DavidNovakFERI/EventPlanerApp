from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_mapping(
        SECRET_KEY='your_secret_key',
    )

    # Register blueprints or routes
    from . import routes
    app.register_blueprint(routes.bp)

    return app