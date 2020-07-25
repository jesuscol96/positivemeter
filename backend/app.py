import os
from flask import Flask
from flask_cors import CORS
from config import Config
from views import *

#App
app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

port = 80

#Routes
app.add_url_rule('/get_score','get_score',get_score, methods = ['GET', 'POST'])
app.add_url_rule('/get_request_count','get_request_count',get_request_count, methods = ['GET'])

#Development server
if __name__ == '__main__':
   app.run(debug = True, port=port)
