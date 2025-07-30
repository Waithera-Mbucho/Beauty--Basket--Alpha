# optimizer.py

import pandas as pd
from scipy.optimize import linprog

def optimize_routine(df, budget):
    """
    Selects the best combination of products to maximize glow_score within budget.
    Assumes 1 unit of each product.

    Parameters:
        df (DataFrame): Must include 'name', 'price', and 'final_score'
        budget (float): Max budget allowed

    Returns:
        selected_products (DataFrame)
    """
    prices = df['price'].values
    scores = df['final_score'].values

    # Convert to minimization problem (negate scores)
    c = -scores

    # Constraint: total price ≤ budget
    A = [prices]
    b = [budget]

    # Bounds: each product can be selected 0 or 1 times (binary selection)
    x_bounds = [(0, 1) for _ in prices]

    # Solve LP relaxation (you can upgrade to integer programming later)
    result = linprog(c, A_ub=A, b_ub=b, bounds=x_bounds, method='highs')

    if result.success:
        selected = result.x.round().astype(int)
        selected_products = df[selected == 1]
        return selected_products
    else:
        print("Optimization failed:", result.message)
        return pd.DataFrame()
