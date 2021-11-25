from flask import Flask
app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def index():
    return "<h1>This application flask framework </h1>"

if __name__ == "__main__":
    app.run()