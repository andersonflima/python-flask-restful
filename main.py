from flask import Flask
from flask_restful import Api, Resource, request


app = Flask(__name__)
api = Api(app)

class Hello(Resource):
    def get():
        if "/" == request.path:
            return 'Hello Wolrd!'
            
api.add_resource(Hello, "/")

if __name__=='__main__':
    app.run('localhost', port=3000)