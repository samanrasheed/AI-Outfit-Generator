AI Outfit Generator

A Flask-based REST API for generating outfit combinations from wardrobeitems and providing color-matching recommendations.

Project Overview

The AI Outfit Generator provides backend APIs for:

Generating outfit combinations from wardrobe items

Matching outfits with an occasion and season

Providing a color palette and outfit match score

Providing color-matching recommendations

The API is built with Python, Flask, Flask-CORS, and Gunicorn and isdeployed on Render.

Features

1. Generate Outfit

Generates an outfit recommendation using:

Wardrobe items

Occasion

Season

Endpoint

POST /api/ai/generate-outfit

Live endpoint

https://ai-outfit-generator-ruy8.onrender.com/api/ai/generate-outfit

Request body

{
  "items": [
    "Black Blazer",
    "White Shirt",
    "Blue Jeans"
  ],
  "occasion": "Casual",
  "season": "Summer"
}

Example response

{
  "data": {
    "colorPalette": [
      "White",
      "Black",
      "Blue"
    ],
    "matchScore": 81,
    "occasion": "Casual",
    "outfit": {
      "items": [
        "Black Blazer",
        "White Shirt",
        "Blue Jeans"
      ]
    },
    "reason": "This outfit is suitable for Casual during Summer.",
    "season": "Summer"
  },
  "success": true
}

2. Color Match

Provides color-matching recommendations for a given color.

Endpoint

POST /api/ai/color-match

Request body

{
  "color": "navy"
}

Validation

The outfit API validates:

Supported occasions

Business Casual

Party

Casual

Formal

Supported seasons

Summer

Winter

Spring

Autumn

At least one wardrobe item, an occasion, and a season are required foroutfit generation.

The color-match API requires a color value.

API Response

Successful responses use a common response structure containing:

{
  "success": true,
  "data": {}
}

Validation and server errors are returned with an appropriate errormessage.

Project Structure

AI-Outfit-Generator/
│
├── app.py
├── requirements.txt
├── README.md
│
├── services/
│   ├── prompt_service.py
│   └── ai_service.py
│
├── validators/
│   └── request_validator.py
│
└── utils/
    ├── response.py
    └── logger.py

Technologies Used

Python 3

Flask

Flask-CORS

Gunicorn

REST API

Render

Postman for API testing

Local Setup

Clone the repository:

git clone <https://github.com/samanrasheed/AI-Outfit-Generator>
cd AI-Outfit-Generator

Create and activate a virtual environment:

python3 -m venv .venv
source .venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Run the Flask application:

python3 app.py

The API will be available locally at:

http://127.0.0.1:5000

Testing with Postman

For the outfit-generation API:

Create a new POST request.

Use:

https://ai-outfit-generator-ruy8.onrender.com/api/ai/generate-outfit

Select Body → raw → JSON.

Send:

{
  "items": [
    "Black Blazer",
    "White Shirt",
    "Blue Jeans"
  ],
  "occasion": "Casual",
  "season": "Summer"
}

A successful request should return success: true together with thegenerated outfit data.

Deployment

The application is deployed on Render using the main Git branch.

Build command:

pip install -r requirements.txt

Start command:

gunicorn app:app

Render automatically redeploys the service when changes are pushed tothe connected GitHub repository.

Current Deployment Status

The live POST /api/ai/generate-outfit endpoint has been successfullytested with Postman and returned a successful response containing:

Outfit items

Color palette

Match score

Occasion

Season

Recommendation reason

Error Handling

The API includes validation and exception handling for invalid requestsand service errors.

During deployment testing, a validation-handling issue causing HTTP 500responses was identified and fixed by making the request validatorreturn the expected error dictionary format.

Project Goal

The goal of this backend is to provide outfit-generation andcolor-matching APIs that can be connected to the project's frontend AIOutfit Generator interface.