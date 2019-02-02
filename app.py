import os.path
import json
import hashlib

from flask import Flask, Response, request, url_for, session, abort, make_response
from flask_cors import CORS
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='secret_xxx'
)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

CORS(app)


class User(UserMixin):

    def __init__(self, id, username, password):
        self.id = id
        self.name = username
        self.password = password

    def __eq__(self, other):
        return self.id == other.id

    def __repr__(self):
        return ''.join(' ' + str(x) for x in [self.id, self.name, self.password])


users = []


def root_dir():  # pragma: no cover
    return os.path.abspath(os.path.dirname(__file__))


def get_file(filename):  # pragma: no cover
    try:
        src = os.path.join(root_dir(), filename)
        # Figure out how flask returns static files
        # Tried:
        # - render_template
        # - send_file
        # This should not be so non-obvious
        return open(src).read()
    except IOError as exc:
        return str(exc)


@app.route('/', methods=['GET'])
def metrics():  # pragma: no cover
    content = get_file('static/index.html')
    return Response(content, mimetype="text/html")


@app.route('/login', methods=['POST'])
def auth():
    if request.method == 'POST':
        if json.loads(request.data)['action'] == 'registration':
            username = json.loads(request.data)['username']
            password = json.loads(request.data)['password']
            id = hashlib.md5((username + password).encode()).hexdigest()
            user = User(id, username, password)
            if user in users:
                resp = make_response('user are exist')
                return resp
            else:
                resp = { 'token': id }
                users.append(user)
                login_user(user)
                return json.dumps(resp)
        else:
            resp = make_response('unknown action')
            return resp
    else:
        return 'somethings gone wrong'


# @app.route('/logout', methods=['post'])
# def logout():
#     if request.method == 'POST':
#         token = json.loads(request.data)['token']
#         position = users.index(User(id))
#         print(position)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def get_resource(path):  # pragma: no cover
    mimetypes = {
        ".css": "text/css",
        ".html": "text/html",
        ".js": "application/javascript",
    }
    complete_path = os.path.join(root_dir(), path)
    ext = os.path.splitext(path)[1]
    mimetype = mimetypes.get(ext, "text/html")
    content = get_file(complete_path)
    return Response(content, mimetype=mimetype)


if __name__ == '__main__':  # pragma: no cover
    app.run()
