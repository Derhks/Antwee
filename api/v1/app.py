from flasgger import Swagger
from flask import Flask
from flask_restful import Api


app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)


if __name__ == '__main__':
    app.run()
