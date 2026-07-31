from flask import Flask, request, jsonify  # import necessary modules from flask
from services.prompt_service import create_outfit_prompt
from services.ai_service import generate_ai_outfit
from validators.request_validator import validate_request
from utils.response import success_response, error_response
from utils.logger import logger

app = Flask(__name__)  # create flask application

@app.route("/")
def home():
    return "Welcome to AI Outfit Generator API"
@app.route("/api/ai/generate-outfit", methods=["POST"])

def generate_outfit(): 
    logger.info("Generate Outfit API called")
    
    data = request.get_json()  # Get user input from the request body
    
    logger.info("Request data received")
    
    validation_error = validate_request(data)
    if validation_error:
        logger.error(f"Validation failed: {validation_error['error']}")
        return jsonify(error_response(validation_error["error"])), 400

    logger.info("Validation successful")
    
    items = data.get("items", [])
    occasion = data.get("occasion", "").strip().title()# Extract occasion from the input and format it
    season = data.get("season", "").strip().title()

    prompt = create_outfit_prompt(items, occasion, season)
    logger.info("Prompt created successfully")
    
    # Return prompt (temporary, until AI API is connected)
    result = generate_ai_outfit(prompt)
    logger.info("AI response generated successfully")


    return jsonify(success_response(result))


if __name__ == "__main__":  #start the  flask server
    app.run(debug=True)
