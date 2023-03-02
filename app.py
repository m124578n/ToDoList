from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# @app.route("/")
# def hello():
#     return "Hello, World!"

class Helloworld(Resource):
    def get(self):
        return {'message':'hello world'}

user_list = []

class User(Resource):

    def get(self, username):
        for user in user_list:
            if user['username'] == username:
                return user
        return {'username': None}, 404
    
    def post(self, username):
        user = {
            'username': username,
            'email': request.form.get('email')
        }
        user_list.append(user)
        return user
    
    def delete(self, username):
        for ind, user in enumerate(user_list):
            if user['username'] == username:
                deleted_user = user_list.pop(ind)
                print(deleted_user)
                return {'note': 'successfully delete'}
            
    def put(self, username):
        user_find = None
        for user in user_list:
            if user['username'] == username:
                user_find = user
        if user_find:
            user_list.remove(user_find)
            user_find['email'] = request.form.get('email')
            user_list.append(user_find)
            return user_find
        
class UserList(Resource):
    """會員列表 """
    def get(self):
        return {'user_list': user_list}
    
api.add_resource(Helloworld, '/Helloworld/')
api.add_resource(User, '/user/<string:username>')
api.add_resource(UserList, '/users/')

if __name__ == '__main__':
    app.run()
