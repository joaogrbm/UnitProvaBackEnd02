from flask import Flask, request
from flask_restful import Resource, Api
from models import Users, init_db
import jwt

app = Flask(__name__)
api = Api(app)

@app.route('/user',methods = ['POST','GET'])
def post(self):
    body = json.loads(request.data)
    newUser = User(nome=body["nome"],
                       idade=body["idade"],
                       login=body["login"],
                       senha=body["senha"])
    NewUser.save()

def get(self, id):
        user = Users.query.filter_by(id=id).first()
        response = {
                "nome": Users.nome,
                "id": Users.id
        }

@app.route('/login',methods = ['POST'])
def login():
    if request.method == 'POST':
        login = request.form['email']
        senha = request.form['password']
        return "Email: " + email + " <br> " + "Password: " + password

class Auth(Resource):
def post(self):
    try:
        key = "password"
        users = json.loads(request.data)
        payload = {
        "user": "João Gabriel",
        "login": users["jgmelo"]
        }
        encoded = jwt.encode(payload, key)
        response = {
        "jwt-token": encoded
        }
        return response
    except:
        return {"error": "Bad request"}

def get(self):
    try:
         token = request.headers.get('authorization')
            payload = jwt.decode(jwt,"password",algorithms=["H256"])
            return {"ok": "ok"}
        except:
            return {"error": "error"}

api.add_Resource(Auth, '/signin')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)