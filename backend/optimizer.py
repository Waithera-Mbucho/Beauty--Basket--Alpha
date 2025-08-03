import pandas as pd
from scipy.optimize import linprog
from typing import Optional

def optimize_routine(
    df: pd.DataFrame,
    min_budget: float = 0.0,
    max_budget: Optional[float] = None
) -> pd.DataFrame:
    """Select the best combination of products to maximize final_score.

    Solves an LP relaxation over 0–1 decisions to pick items within [min_budget, max_budget].
    """
    if max_budget is None:
        raise ValueError("max_budget is required")

    # Ensure budgets are floats
    max_b: float = float(max_budget)
    min_b: float = float(min_budget)

    # Extract price & score arrays
    prices = df["price"].values.astype(float)
    scores = df["final_score"].values.astype(float)

    # Objective: maximize score → minimize negative score
    c = -scores

    # Upper‐bound constraint: sum(prices * x) <= max_b
    A_ub = [prices]
    b_ub = [max_b]

    # Lower‐bound constraint: sum(prices * x) >= min_b → -(prices * x) <= -min_b
    if min_b > 0:
        A_ub.append(-prices)
        b_ub.append(-min_b)

    # Bounds: 0 <= x_i <= 1
    bounds = [(0, 1) for _ in prices]

    # Solve with the HiGHS solver
    result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method="highs")

    if result.success:
        # Round to 0 or 1 and filter
        choice = result.x.round().astype(int)
        return df[choice == 1].copy()
    else:
        print("Optimization failed:", result.message)
        return pd.DataFrame()
