import os, time, json
from flask import Flask, request, Response
from flask_cors import CORS, cross_origin
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

from models.tasks import Tasks
from models.users import Users, Auth

app = Flask(__name__)
cors = CORS(app)
jwt = JWTManager(app)

app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET')

@app.route('/')
def index():
    return {
        'version': '1.0.0',
        'app': 'PVM API',
        'url': '/api/%method%'
    }

@app.route('/api/time')
@cross_origin()
def api_time():
    return {
        'time': time.time()
    }

@app.route('/api/login', methods=['POST'])
@cross_origin()
def api_login():
    credentials = request.json

    if not credentials: return {
        'error': 'Request body is empty or not valid!'
    }

    username = credentials.get('username', None)
    password = credentials.get('password', None)

    if username and password:
        auth = Auth(username, password)
        if auth.jwt:
            return Response(
                response="OK",
                status=200,
                headers={
                    'Authorization': 'Bearer ' + auth.jwt
                },
                content_type='application/json'
            )
        else:
            return {
                'error': 'Invalid username or password!'
            }
    else:
        return {
            'error': 'Need credentials info!'
        }


@app.route('/api/tasks', methods=['GET'])
@jwt_required
@cross_origin()
def api_tasks():
    user = Users.objects(password=get_jwt_identity()).first()
    user_id = json.loads(user.to_json()).get('_id', None)

    if user_id and user_id.get('$oid', None):
        tasks = Tasks.objects(uid=user_id.get('$oid'))
        return {
            'dbg': tasks.to_json()
        }
    else:
        return {
            'error': 'Something gonna wrong... The required _id-fields is not found in query set!'
        }


app.run(
    host=os.environ.get('API_HOST'),
    debug=bool(os.environ.get('API_DEBUG')),
    port=os.environ.get('API_PORT')
)
