from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/game", methods=['GET', 'POST'])
def game():
    return "almost there!"

if __name__ == "__main__":
    app.run(debug=True)
