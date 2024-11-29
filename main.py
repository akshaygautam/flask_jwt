from flask import Flask, jsonify
from extentions import db, jwt
from auth import auth_bp
from users import user_bp
from models import User


def create_app():

    app = Flask(__name__)

    # read envs
    app.config.from_prefixed_env()
    
    # initialize extenstions
    db.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(auth_bp,url_prefix='/auth')
    app.register_blueprint(user_bp,url_prefix='/users')
    

    @jwt.user_lookup_loader
    def user_lookup_callback(__jwt_header,jwt_data):
        identity= jwt_data['sub']
        return User.query.filter_by(username=identity).one_or_none()

    #special previlage

    @jwt.additional_claims_loader
    def make_additional_permissions(identity):
        if identity == "akshay":
            return {"is_admin":True}
        else:
            return {"is_admin": False}
    # jwt-error-handler

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_data):
        return jsonify({"message":"Token has expired", "error":"token_expired"}), 401 
    
    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return jsonify({"message":"Verification failed", "error":"invalid_token"}), 401 


    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return jsonify({"message":"Request does not contains valid token", "error":"auth_error"}), 401 
    return app
