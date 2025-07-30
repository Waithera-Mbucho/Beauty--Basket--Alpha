# factors/ingredient_scoring.py

import ast

# ✨ Science-backed ingredient weights
INGREDIENT_SCORES = {
    "niacinamide": {"hydration": 0.4, "acne": 0.6, "tone_evenness": 0.3},
    "hyaluronic acid": {"hydration": 1.0},
    "retinol": {"firmness": 0.8, "acne": 0.4},
    "glycerin": {"hydration": 0.8},
    "salicylic acid": {"acne": 1.0},
    "peptides": {"firmness": 0.6},
    "vitamin c": {"tone_evenness": 0.7},
    "squalane": {"hydration": 0.5},
    "ceramides": {"hydration": 0.6, "sensitivity": 0.5},
    "licorice root": {"tone_evenness": 0.6},
}

def score_ingredients(ingredient_list, focus_area="hydration"):
    """Compute total ingredient score for a given skin concern."""
    total = 0
    for ing in ingredient_list:
        ing = ing.lower().strip()
        if ing in INGREDIENT_SCORES and focus_area in INGREDIENT_SCORES[ing]:
            total += INGREDIENT_SCORES[ing][focus_area]
    return total
