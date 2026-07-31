from flask import Flask, request, jsonify  # import necessary modules from flask
from services.prompt_service import create_outfit_prompt
from services.ai_service import generate_ai_outfit

app = Flask(__name__)  # create flask application

@app.route("/")
def home():
    return "Welcome to AI Outfit Generator API"
@app.route("/api/ai/generate-outfit", methods=["POST"])
def generate_outfit(): 
    data = request.get_json()  # Get user input from the request body
    items = data.get("items", [])
    occasion = data.get("occasion", "").strip().title()# Extract occasion from the input and format it
    season = data.get("season", "").strip().title()
      
     
    valid_seasons = ["Summer", "Winter", "Spring", "Autumn"]
    valid_occasions = [
    "Business Casual",
    "Party",
    "Casual",
    "Formal"
]
    if not items:
        return jsonify({
            "error": "Please provide at least one wardrobe item."
        }), 400

    if occasion not in valid_occasions:
        return jsonify({
            "error": "Invalid occasion."
    }), 400

    if season not in valid_seasons:
        return jsonify({
            "error": "Invalid season. Choose Summer, Winter, Spring or Autumn."
    }), 400
    prompt = create_outfit_prompt(items, occasion, season)
        # Return prompt (temporary, until AI API is connected)
    result = generate_ai_outfit(prompt)

    return jsonify(result)


if __name__ == "__main__":  #start the  flask server
    app.run(debug=True)
