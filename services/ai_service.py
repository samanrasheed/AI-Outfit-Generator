import random
def generate_ai_response(items=None, occasion=None, season=None, color=None):

    # # Generate mock outfit recommendation
    if items:

        return {
            "outfit": {
                "items": items
            },
            "occasion": occasion,
            "season": season,
            "matchScore": random.randint(80, 100),
            "colorPalette": [
                "White",
                "Black",
                "Blue"
            ],
            "reason": f"This outfit is suitable for {occasion} during {season}."
        }

    # # Generate mock color recommendations
    if color:

        return {
            "inputColor": color,
            "matchingColors": [
                {
                    "color": "White",
                    "match": 98,
                    "description": f"White pairs well with {color}."
                },
                {
                    "color": "Beige",
                    "match": 94,
                    "description": f"Beige creates an elegant combination with {color}."
                }
            ]
        }
    raise ValueError("No valid input provided.")
