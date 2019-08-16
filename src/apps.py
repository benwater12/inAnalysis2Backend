import os
from flask import Flask
from flask_restful import Api
from flask_login import LoginManager
from flask_cors import CORS
from service.userService.controller.signin import Singin
from service.userService.controller.signup import Singup
from datetime import timedelta
import logging
import sys
sys.dont_write_bytecode = True #disable __pycache__
from params import params

par=params()
app = Flask(__name__)
app.config['SECRET_KEY'] = par.secretKey
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=1)
api = Api(app)
login_manager = LoginManager(app)
cors = CORS(app)

# bind api
api.add_resource(Singin, "/user/signin")
api.add_resource(Singup, "/user/signup")


if __name__ == "__main__":
    if '--debug' in sys.argv:
        logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] %(message)s')
    else:
        logging.basicConfig(level=logging.INFO , format='[%(levelname)s] %(message)s')
    logging.info(f'Inanalysis running at port {par.port}')
    app.run(debug='--debug' in sys.argv,port=par.port,host='0.0.0.0')