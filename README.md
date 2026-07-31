# AI Outfit Generator

## Project Overview

AI Outfit Generator is a Flask-based REST API that generates outfit recommendations based on a user's wardrobe, occasion, and season.

The project validates user input, creates an AI prompt, sends it to an AI service, and returns a structured JSON response.

---

## Features

- Generate outfit recommendations
- Input validation
- Prompt generation
- AI service integration (currently mock implementation)
- Standardized API responses
- Logging for API requests and errors

---

## Tech Stack

- Python 3
- Flask
- REST API
- JSON
- Git & GitHub

---

## Project Structure

```
AI-Outfit-Generator/

├── app.py
├── services/
│   ├── ai_service.py
│   └── prompt_service.py
│
├── validators/
│   └── request_validator.py
│
├── utils/
│   ├── logger.py
│   └── response.py
│
├── prompts/
├── routes/
├── requirements.txt
├── README.md
└── .gitignore
```

---

## API Endpoint

### Generate Outfit

**POST**

```
/api/ai/generate-outfit
```

### Request Body

```json
{
    "items": [
        "Black Blazer",
        "White Shirt",
        "Blue Jeans"
    ],
    "occasion": "Business Casual",
    "season": "Summer"
}
```

---

## Sample Response

```json
{
    "success": true,
    "data": {
        "message": "AI service will be connected here."
    }
}
```

---

## Installation

Clone the repository

```bash
git clone <repository-url>
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python3 app.py
```

The API will run on:

```
http://127.0.0.1:5000
```

---

## Future Improvements

- Connect OpenAI/Grok API
- AI Color Matcher endpoint
- Outfit history
- Authentication
- Unit testing
- Docker support

---

## Author

**Saman Rasheed**