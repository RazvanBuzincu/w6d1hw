from flask import Flask 
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager


#internal imports 
from .blueprints.site.routes import site 
from config import Config 
from .models import login_manager, db 
from .blueprints.auth.routes import auth
from .helpers import JSONEncoder
from .blueprints.api.routes import api

#instantiating our Flask app
app = Flask(__name__) #passing in the __name__ variable which just takes the name of the folder we're in
#add this
app.config.from_object(Config)
jwt = JWTManager(app)


#wrap our app in login_manager so we can use it wherever in our app
login_manager.init_app(app)
login_manager.login_view = 'auth.sign_in' 
login_manager.login_message = "Hey you! Log in please!"
login_manager.login_message_category = 'warning'


#we are going to use a decorator to create our first route
# @app.route("/")
# def hello_world():
#     return "<p>Hello World!</p>"


app.register_blueprint(site)
app.register_blueprint(auth)
app.register_blueprint(api)


#instantiating our datbase & wrapping our app
db.init_app(app)
migrate = Migrate(app, db)
app.json_encoder = JSONEncoder
cors = CORS(app)