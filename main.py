from flask import Flask
application = Flask(__name__)

@application.route('/',methods=["GET","POST"])
def index():
    return "<h1><This application flask framework</h1>"

if __name__ == "__main__":
    application.run()