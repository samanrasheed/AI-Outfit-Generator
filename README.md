# AI Outfit Generator

A Flask-based REST API for generating outfit combinations from wardrobe items and providing color-matching recommendations.

## Project Overview

The **AI Outfit Generator** provides backend APIs for:

- Generating outfit combinations from wardrobe items
- Matching outfits with an occasion and season
- Providing a color palette and outfit match score
- Providing color-matching recommendations

The API is built with **Python, Flask, Flask-CORS, and Gunicorn** and is deployed on **Render**.

## Features

### 1. Generate Outfit

Generates an outfit recommendation using:

- Wardrobe items
- Occasion
- Season

**Endpoint**

```text
POST /api/ai/generate-outfit
```

**Live Endpoint**

```text
https://ai-outfit-generator-ruy8.onrender.com/api/ai/generate-outfit
```

**Request Body**

```json
{
  "items": [
    "Black Blazer",
    "White Shirt",
    "Blue Jeans"
  ],
  "occasion": "Casual",
  "season": "Summer"
}
```

**Example Response**

```json
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
```

### 2. Color Match

Provides color-matching recommendations for a given color.

**Endpoint**

```text
POST /api/ai/color-match
```

**Request Body**

```json
{
  "color": "navy"
}
```

## Validation

The outfit API validates the following:

### Supported Occasions

- Business Casual
- Party
- Casual
- Formal

### Supported Seasons

- Summer
- Winter
- Spring
- Autumn

At least one wardrobe item, an occasion, and a season are required for outfit generation.

The color-match API requires a color value.

## API Response

Successful responses use the following common response structure:

```json
{
  "success": true,
  "data": {}
}
```

Validation and server errors are returned with an appropriate error message.

## Project Structure

```text
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
```

## Technologies Used

- Python 3
- Flask
- Flask-CORS
- Gunicorn
- REST API
- Render
- Postman

## Local Setup

Clone the repository:

```bash
git clone <https://github.com/samanrasheed/AI-Outfit-Generator>
cd AI-Outfit-Generator
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Flask application:

```bash
python3 app.py
```

The API will be available locally at:

```text
http://127.0.0.1:5000
```

## Testing with Postman

For the outfit-generation API:

1. Create a new **POST** request.
2. Use the following URL:

```text
https://ai-outfit-generator-ruy8.onrender.com/api/ai/generate-outfit
```

3. Select **Body → raw → JSON**.
4. Send the following request:

```json
{
  "items": [
    "Black Blazer",
    "White Shirt",
    "Blue Jeans"
  ],
  "occasion": "Casual",
  "season": "Summer"
}
```

5. A successful request should return `success: true` together with the generated outfit data.

## Deployment

The application is deployed on **Render** using the `main` Git branch.

**Build Command:**

```bash
pip install -r requirements.txt
```

**Start Command:**

```bash
gunicorn app:app
```

Render automatically redeploys the service when changes are pushed to the connected GitHub repository.

## Current Deployment Status

The live `POST /api/ai/generate-outfit` endpoint has been successfully deployed and tested using Postman.

The endpoint successfully returns:

- Outfit items
- Color palette
- Match score
- Occasion
- Season
- Recommendation reason

## Error Handling

The API includes request validation and exception handling for invalid requests and service errors.

During deployment testing, a validation-handling issue causing HTTP 500 responses was identified and fixed by making the request validator return the expected error dictionary format.

## AI Integration Status

The current `ai_service.py` uses a temporary/mock response for testing the API structure and deployment.

A real AI provider such as Grok or OpenAI can be integrated later when the required API credentials are provided by the team.

## Project Goal

The goal of this backend is to provide outfit-generation and color-matching APIs that can be connected to the project's frontend AI Outfit Generator interface.