def create_outfit_prompt(items, occasion, season):
    prompt = f"""
You are an expert AI fashion stylist.

Task:
Generate one outfit recommendation using ONLY the wardrobe items provided.

Wardrobe Items:
{', '.join(items)}

Occasion:
{occasion}

Season:
{season}

Rules:
1. Use only the wardrobe items provided.
2. Do not recommend additional clothing items.
3. Generate the outfit according to the selected occasion and season.
4. Recommend suitable accessories.
5. Suggest matching color combinations.
6. Explain why each item matches.
7. Avoid duplicate outfit items and duplicate color combinations.
8. Return ONLY valid JSON.
"""

    return prompt