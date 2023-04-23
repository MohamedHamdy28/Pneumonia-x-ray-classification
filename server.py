from flask import Flask, request, g, session, redirect, send_from_directory, jsonify, url_for
from werkzeug.exceptions import NotFound
from functools import wraps
import os, uuid
import model

app = Flask(__name__)
app.secret_key = 'super-secret'



class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password
    
    def __str__(self):
        return f'User(id={self.id}, username={self.username}, password={self.password})'


users = {
    'admin_id'  : User(id='admin_id', username='admin', password='apass'),
    'client1_id': User(id='client1_id', username='client1', password='1pass'),
    'client2_id': User(id='client2_id', username='client2', password='2pass')
}



def get_user(user_id: str):
    return users.get(user_id, None)

def get_user_by(username: str, password: str):
    for user in users.values():
        if user.username == username and user.password == password:
            return user
    return None



def set_user(user: User):
    session.clear()
    session['user_id'] = user.id

@app.before_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = get_user(user_id)



def login_required(f):
    @wraps(f)
    def wrapped_func(*args, **kwargs):
        if g.user is None:
            response = {'error': "You are not logged in"}
            return jsonify(response), 401
        return f(*args, **kwargs)
    return wrapped_func

def logout_required(f):
    @wraps(f)
    def wrapped_func(*args, **kwargs):
        if g.user is not None:
            response = {'error': "You are logged in"}
            return jsonify(response), 409
        return f(*args, **kwargs)
    return wrapped_func



@app.route('/')
def index():
    return send_from_directory('client/build', 'index.html')



@app.route("/<path:path>")
def home(path):
    try:
        return send_from_directory('client/build', path)
    except NotFound:
        return redirect('/')



@app.route('/api/getuser')
def getuser():
    response = {}
    if g.user is not None:
        response['username'] = g.user.username
    print(f'getuser(): {response}')
    return jsonify(response)



@app.route('/api/logout')
@login_required
def logout():
    session.clear()
    response = {'message': "You have logged out sucessfully"}
    return jsonify(response)



@app.route('/api/login', methods=['POST'])
@logout_required
def login():
    username = request.json.get('username', '')
    password = request.json.get('password', '')

    user = get_user_by(username, password)
    if user is None:
        response = {'error': 'Invalid username or password'}
        return jsonify(response), 401
    else:
        set_user(user)
        response = {
            'username': user.username
        }
        return jsonify(response)


@app.route('/api/upload', methods=['POST'])
def upload_file():
    
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']


    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    allowed_extensions = ['.jpeg', '.png']

    file_extension = str(os.path.splitext(file.filename)[1])
    print(file_extension)
    if file_extension not in allowed_extensions:
        return jsonify({'error': f"File should have one of {allowed_extensions} extensions"}), 400

    filename = str(uuid.uuid4()) + file_extension

    
    filepath = os.path.join('imageStorage', filename)
    file.save(filepath)

    return jsonify({'result': model.get_prediction(filepath) })




if __name__ == '__main__':
    app.run(debug=True)
