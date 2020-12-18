from flask import Flask
import logging as logger
logger.basicConfig(level="DEBUG")


FlaskAppInstance = Flask(__name__)

if __name__ == '__main__':
    logger.debug("Starting the application")

    FlaskAppInstance.run(host="0.0.0.0",port=5000,debug=True,use_reloader=True)
