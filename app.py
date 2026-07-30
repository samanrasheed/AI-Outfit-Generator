from flask import Flask, request, jsonify  # import necessary modules from flask

app = Flask(__name__)  # create flask application

@app.route("/")
def home():
    return "Welcome to AI Outfit Generator API"
@app.route("/api/ai/generate-outfit", methods=["POST"])
def generate_outfit(): 
    data = request.get_json()  # Get user input from the request body
    
    # Logic to generate outfit based on user input
    return jsonify({                                 
        "message": "Outfit generated successfully!", #flask send the JSON back to frontend
        "received_data": data})

if __name__ == "__main__":  #start the  flask server
    app.run(debug=True)
