from flask import Flask, request, jsonify  # import necessary modules from flask
from services.prompt_service import (
    create_outfit_prompt,
    create_color_match_prompt
)
from services.ai_service import generate_ai_response
from validators.request_validator import (
    validate_outfit_request,
    validate_color_request
)
from utils.response import success_response, error_response
from utils.logger import logger
from flask_cors import CORS

app = Flask(__name__)  # create flask application
CORS(app)  # Enable CORS for the Flask app

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to AI Outfit Generator API",
        "status": "running"
    })
@app.route("/api/ai/generate-outfit", methods=["POST"])


def generate_outfit(): 
    logger.info("Generate Outfit API called")
    
    data = request.get_json()  # Get user input from the request body
    
    logger.info("Request data received")
    
    validation_error = validate_outfit_request(data)
    if validation_error:
        logger.error(f"Validation failed: {validation_error['error']}")
        return jsonify(error_response(validation_error["error"])), 400

    logger.info("Validation successful")
    
    items = data.get("items", [])
    # Extract occasion and format it
    occasion = data.get("occasion", "").strip().title()
    season = data.get("season", "").strip().title()

    # Prompt is created for future Grok/OpenAI integration.
    prompt = create_outfit_prompt(items, occasion, season)
    logger.info("Prompt created successfully")
    
    
    try:
        result = generate_ai_response(
            items=items,
            occasion=occasion,
            season=season
        )
        logger.info("AI response generated successfully")
        return jsonify(success_response(result))
    except Exception as e:

        logger.error(f"AI Service Error: {e}")

        return jsonify(
            error_response(
                "Unable to generate outfit at the moment. Please try again later."
            )
        ), 500

@app.route("/api/ai/color-match", methods=["POST"])

def color_match():

    data = request.get_json()

    validate_error = validate_color_request(data)

    if validate_error:
        logger.error(f"Validation failed: {validate_error['error']}")
        return jsonify(error_response(validate_error["error"])), 400

    color = data["color"].strip().title()

    # Prompt is created for future Grok/OpenAI integration.
    prompt = create_color_match_prompt(color)

    logger.info("Color extracted successfully")

    try:

        result = generate_ai_response(
            color=color
        )

        logger.info("Color recommendations generated successfully")

        return jsonify(success_response(result))

    except Exception as e:

        logger.exception("AI Service Error")

        return jsonify(
            error_response(
                "Unable to generate color recommendations."
            )
        ), 500

if __name__ == "__main__":  #start the  flask server
    app.run(debug=True)
