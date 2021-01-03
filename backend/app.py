import os, time
from flask import Flask
from flask_cors import CORS, cross_origin

from mongodb import MongoDB

app = Flask(__name__)
cors = CORS(app)
mongo = MongoDB()

@app.route('/')
def index():
    return {
        'version': '1.0.0',
        'app' : 'PVM API',
        'url' : '/api/%method%'
    }

@app.route('/api/time')
@cross_origin()
def api_time():
    return {
        'time': time.time()
    }

@app.route('/api/fetch/<collection>')
def api_fetch(collection):
    return {
        collection: mongo.fetch(collection)
    }


app.run(
    host=os.environ.get('API_HOST'),
    debug=bool(os.environ.get('API_DEBUG')),
    port=os.environ.get('API_PORT')
)
