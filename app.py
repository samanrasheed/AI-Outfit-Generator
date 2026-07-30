from flask import Flask, request, jsonify  # import necessary modules from flask
from services.prompt_service import create_outfit_prompt

app = Flask(__name__)  # create flask application

@app.route("/")
def home():
    return "Welcome to AI Outfit Generator API"
@app.route("/api/ai/generate-outfit", methods=["POST"])
def generate_outfit(): 
    data = request.get_json()  # Get user input from the request body
      items = data["items"]
      occasion = data["occasion"]
      season = data["season"] # Extract season from the input
    
    if not items:
    return jsonify({
        "error": "Please provide at least one wardrobe item."
    }), 400
    if not occasion:
    return jsonify({
        "error": "Occasion is required."
    }), 400
    if not season:
    return jsonify({
        "error": "Season is required."
    }), 400
    prompt = create_outfit_prompt(items, occasion, season)
    # Logic to generate outfit based on user input                                
       return jsonify({
    "message": "Prompt created successfully!",
    "prompt": prompt
})

if __name__ == "__main__":  #start the  flask server
    app.run(debug=True)
