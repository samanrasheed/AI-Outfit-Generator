VALID_SEASONS = [
    "Summer",
    "Winter",
    "Spring",
    "Autumn",
]

VALID_OCCASIONS = [
    "Business Casual",
    "Party",
    "Casual",
    "Formal",
]


def validate_outfit_request(data):
    items = data.get("items", [])
    occasion = data.get("occasion", "").strip().title()
    season = data.get("season", "").strip().title()

    if not items:
        return {
            "error": "Please provide at least one wardrobe item."
        }

    # Check required fields
    if not occasion:
        return {
            "error": "Occasion is required."
        }

    if not season:
        return {
            "error": "Season is required."
        }

    # Validate allowed values
    if occasion not in VALID_OCCASIONS:
        return {
            "error": "Invalid occasion."
        }

    if season not in VALID_SEASONS:
        return {
            "error": "Invalid season. Choose Summer, Winter, Spring or Autumn."
        }

    return None


def validate_color_request(data):
    color = data.get("color", "").strip()

    if not color:
        return {
            "error": "Color is required."
        }

    return None