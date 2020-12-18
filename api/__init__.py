from flask_restful import Api
from app import flaskAppInstance
from .Task import Task

restServer = Api(flaskAppInstance)
restServer.add_resource(Task, "/q/intern")
