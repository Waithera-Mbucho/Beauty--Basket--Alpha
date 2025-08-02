import ast

from flask import Flask, request, render_template
import pandas as pd

from optimizer import optimize_routine
from factors import calculate_glow_scores

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    products = None
    if request.method == 'POST':
        # Get budget from form, defaulting to 50 if invalid
        try:
            budget = float(request.form.get('budget', 50))
        except ValueError:
            budget = 50

        # Get optional focus area (e.g., "hydration", "acne", "glow")
        focus_area = request.form.get('focus_area', None)

        # Load product data
        df = pd.read_csv('data/products.csv')
        # Convert ingredient strings to lists
        df['ingredients'] = df['ingredients'].apply(ast.literal_eval)

        # Calculate glow (and ingredient-based) scores
        df = calculate_glow_scores(df, focus_area=focus_area)

        # Optimize product mix under the given budget
        selected = optimize_routine(df, budget)

        # Prepare results for the template
        products = selected.to_dict(orient='records')

    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
