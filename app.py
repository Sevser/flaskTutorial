import os.path
import json
import hashlib

from flask import Flask, Response, request, redirect, url_for, session, abort, render_template, make_response, abort, g
from flask_cors import CORS
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

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

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class User(UserMixin):

    def __init__(self, id, username, password):
        self.id = id
        self.name = username
        self.password = password

    def __eq__(self, other):
        return self.id == other.id

    def __repr__(self):
        return ''.join(str(x) + ' 'for x in [self.id, self.name, self.password])

class Tiktactoe:
    """
    field - номер от 0 до 8 - ячейка на доске
    012
    345
    678


    """
    def __init__(self, typegame, turn, firstUser, secondUser='bot'):
        self.firstUser = firstUser
        self.secondUser = secondUser
        self.firstUser = turn
        self.secondUser = (turn + 1) % 2
        self.desk = [0]*9
        self.turn = turn
        self.id = hashlib.md5((firstUser + secondUser).encode()).hexdigest()
        self.typegame = typegame

    def is_id_correct(self, id_of_user):
        return id_of_user == self.firstUser.id or id_of_user == self.secondUser.id

    def get_desk(self):
        json.dumps(self.desk)

    def get_space_to_fill(self):
        return json.loads(request.data)['space']


    def is_anybody_won(self):
        if self.desk[0] == self.desk[1] == self.desk[2] != 0:
            return True
        elif self.desk[3] == self.desk[4] == self.desk[5] != 0:
            return True
        elif self.desk[6] == self.desk[7] == self.desk[8] != 0:
            return True
        elif self.desk[0] == self.desk[3] == self.desk[6] != 0:
            return True
        elif self.desk[1] == self.desk[4] == self.desk[7] != 0:
            return True
        elif self.desk[2] == self.desk[5] == self.desk[8] != 0:
            return True
        elif self.desk[0] == self.desk[4] == self.desk[8] != 0:
            return True
        elif self.desk[2] == self.desk[4] == self.desk[6] != 0:
            return True
        return False

    def is_desk_filled(self):
        if self.desk.count(0) == 0:
            return True
        return False

    """здесь надо удалять интсанс и перенаправлять"""
    def finish_the_game(self, lastTurn):
        if self.is_desk_filled():
            print('Ничья')
        else:
            print('Игрок {} победил'.format(lastTurn))


    def make_turn(self):
        space = self.get_space_to_fill()
        if self.desk[space] == 0:
            self.desk[space] = self.turn + 1
            self.turn = (self.turn + 1) % 2
            return True
        return False








winner = []
users = []
games = []

users.append(User(hashlib.md5(('lox1' + 'lox1').encode()).hexdigest(), 'lox1', 'lox1'))
users.append(User(hashlib.md5(('lox2' + 'lox2').encode()).hexdigest(), 'lox2', 'lox2'))


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

@app.before_request
def before_request():
    g.user = current_user

@app.route('/getuser', methods=['POST'])
def get_user():
    if json.loads(request.data)['action'] == 'getallusers':
        names = []
        for user in users:
            names.append({"username": user.name})
        #print(names)

        resp = {"users": names}
        return json.dumps(resp)


@app.route('/tiktactoe', methods=['POST', 'GET', 'PUT'])
def tiktactoe():
    if request.method == 'POST':
        winner.append(g.user)
        if json.loads(request.data)['action'] == 'play':
            typegame = json.loads(request.data)['typegame']
            turn = json.loads(request.data)['selectturn']
            if typegame == "PlayAlone":
                """возможно, стоит поменять с учетом current_user"""
                currentGame = Tiktactoe(typegame, turn, json.loads(request.data)['token'])
                games.append(currentGame)
                resp = {
                    "status": "success",
                    "description": "zaebis",
                    "idgame": currentGame.id
                }

            else:
                resp = {
                    "status": "failed",
                    "description": "you can only play alone",
                    "idgame": ""
                }
        else:
            resp = {
                "status": "failed",
                "description": "check your choise, fool",
                "idgame": ""
            }
        return json.dumps(resp)
    elif request.method == 'PUT':
        if json.loads(request.data)['action'] == 'maketurn':
            for game in games:
                if True: #здесь должна быть проверка пользователя методом Game.is_id_correct
                    game.make_turn()
                    if game.is_desk_filled():
                        return json.dumps('Ничья, лол ебать как так' + str(game.desk))
                    elif game.is_anybody_won():
                        return json.dumps('Ты победил, умница, красавица, лох')
                    return json.dumps(game.desk)
            return json.dumps(1)
    elif request.method == 'GET':
        user = g.user
        return json.dumps(user)


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
                resp = {'token': id, 'username': username}
                users.append(user)
                login_user(user)
                return json.dumps(resp)
        elif json.loads(request.data)['action'] == 'login':
            username = json.loads(request.data)['username']
            password = json.loads(request.data)['password']
            id = hashlib.md5((username + password).encode()).hexdigest()
            user = User(id, username, password)
            if user in users:
                resp = {'token': id, 'username': username}
                users.append(user)
                login_user(user)
                return json.dumps(resp)
            else:
                resp = make_response('user are not exist')
                return resp
        else:
            return abort(404)
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
