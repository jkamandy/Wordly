from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sedfwesef'
    
    from .views import views1
    from .auth import auth
    
    app.register_blueprint(views1, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    return app