   
valid_seasons = [
        "Summer",
        "Winter",
        "Spring",
        "Autumn",
    ]
valid_occasions = [
        "Business Casual",
        "Party",
        "Casual",
        "Formal",
    ]
def validate_outfit_request(items, occasion, season):
    if not items:
        return jsonify({
            "error": "Please provide at least one wardrobe item."
        }), 400

    # First validation check for the occasion and season.
    if not occasion:
        return jsonify({"error": "Occasion is required."}), 400

    if not season:
        return jsonify({"error": "Season is required."}), 400

    # Second validation is to ensure the entered values are allowed.
    if occasion not in valid_occasions:
        return jsonify({
            "error": "Invalid occasion."
        }), 400

    if season not in valid_seasons:
        return jsonify({
            "error": "Invalid season. Choose Summer, Winter, Spring or Autumn."
        }), 400

    return None

def validate_color_request(data):

    color = data.get("color", "").strip()

    if not color:
        return {
            "error": "Color is required."
        }

    return None