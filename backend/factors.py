# factors.py

import pandas as pd

from ingredients import score_ingredients

def normalize(series):
    max_val = series.max()
    min_val = series.min()
    if max_val == min_val:
        return pd.Series(0, index=series.index)
    return (series - min_val) / (max_val - min_val)


def calculate_glow_scores(df, weights=None, focus_area=None):
    df = df.copy()
    if df.empty:
        return df

    required = {'tone_evenness', 'surface_evenness', 'firmness', 'glow', 'ingredients'}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    default_weights = {
        'tone_evenness': 0.30,
        'surface_evenness': 0.25,
        'firmness': 0.25,
        'glow': 0.20
    }
    if weights:
        default_weights.update(weights)

    # Normalize skin attributes
    df['tone_evenness_score'] = normalize(df['tone_evenness'])
    df['surface_evenness_score'] = normalize(df['surface_evenness'])
    df['firmness_score'] = normalize(df['firmness'])
    df['glow_radiance_score'] = normalize(df['glow'])

    # Calculate glow score
    df['glow_score'] = (
        default_weights['tone_evenness'] * df['tone_evenness_score'] +
        default_weights['surface_evenness'] * df['surface_evenness_score'] +
        default_weights['firmness'] * df['firmness_score'] +
        default_weights['glow'] * df['glow_radiance_score']
    )
    # Score by ingredients if a focus area is given.
    # The 'ingredients' column should already contain lists (parsed upstream).
    if focus_area:
        
         df['ingredient_score'] = df['ingredients'].apply(
            lambda x: score_ingredients(x, focus_area)
        )
         df['ingredient_score'] = normalize(df['ingredient_score'])
         df['final_score'] = 0.7 * df['glow_score'] + 0.3 * df['ingredient_score']
    else:
         df['final_score'] = df['glow_score']

    return df