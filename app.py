from flask import Flask

app = Flask(__name__)  # create flask application

@app.route("/")
def home():
    return "Welcome to AI Outfit Generator API"

if __name__ == "__main__":  #start the  flask server
    app.run(debug=True)
