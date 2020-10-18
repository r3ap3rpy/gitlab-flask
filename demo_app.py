from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/cicd")
def cicd():
    return "GitLab is awesome!"

if __name__ == '__main__':
    app.run(host="localhost", port = 8080, debug = True)