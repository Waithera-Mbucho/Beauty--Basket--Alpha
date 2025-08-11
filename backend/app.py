import ast
import os
from typing import List, Dict, Optional

from flask import Flask, request, render_template
import pandas as pd

from optimizer import optimize_routine
from factors import calculate_glow_scores

app = Flask(__name__, template_folder='templates')

@app.route("/", methods=["GET", "POST"])
def index():
    products: Optional[List[Dict]] = None

    if request.method == "POST":
        # 1) Parse budget (either "NN" or "NN-MM")
        budget_raw = request.form.get("budget", "50").strip()
        try:
            if "-" in budget_raw:
                min_str, max_str = budget_raw.split("-", 1)
                min_budget = int(float(min_str))
                max_budget = int(float(max_str))
            else:
                min_budget = 0
                max_budget = int(float(budget_raw))
        except ValueError:
            # fallback defaults
            min_budget, max_budget = 0, 50

        # 2) Parse optional focus area
        focus_area = request.form.get("focus_area") or None

        # 3) Load your product data relative to this file
        csv_path = os.path.join(os.path.dirname(__file__), "products.csv")
        df = pd.read_csv(csv_path)

        # 4) Parse 'ingredients' string-lists once for downstream use
        if "ingredients" in df.columns:
            df["ingredients"] = df["ingredients"].apply(ast.literal_eval)

        # 5) Compute your glow scores
        df = calculate_glow_scores(df, focus_area=focus_area)

        # 6) Run the optimizer
        selected_df = optimize_routine(df, min_budget, max_budget)

        # 7) Prepare for the template
        if selected_df is None:
            products = []
        else:
            products = selected_df.to_dict(orient="records")

    return render_template("index.html", products=products)


if __name__ == "__main__":
    app.run(debug=True)
