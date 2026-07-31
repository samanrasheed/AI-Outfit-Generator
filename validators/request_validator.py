valid_seasons = [
    "Summer", 
    "Winter", 
    "Spring", 
    "Autumn"]
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
    #first validation check for the occasion and season, if not provided return error message
    if not occasion:
        return jsonify({"error": "Occasion is required."}), 400
    

    if not season:
        return jsonify({"error": "Season is required."}), 400
    #second validation is the value user enter is allowed or not.
    if occasion not in valid_occasions:
        return jsonify({
            "error": "Invalid occasion."
    }), 400

    if season not in valid_seasons:
        return jsonify({
            "error": "Invalid season. Choose Summer, Winter, Spring or Autumn."
    }), 400
    return none