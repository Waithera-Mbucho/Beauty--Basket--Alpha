
import json
import pandas as pd
import os
import sys

# The JSON file you uploaded
JSON_FILENAME = "graphql.json"

def main():
    # 1) Ensure file exists
    if not os.path.exists(JSON_FILENAME):
        print(f" File not found: {JSON_FILENAME}")
        sys.exit(1)

    # 2) Load the JSON
    with open(JSON_FILENAME, 'r') as f:
        data = json.load(f)

    # 3) Drill into the product list (no pagination here)
    items = (
        data
        .get('data', {})
        .get('Page', {})
        .get('content', {})
        .get('items', [])
    )

    # 4) Extract the fields you want
    rows = []
    for item in items:
        sale_price = item.get('salePrice') or item.get('listPrice')
        rows.append({
            'product_brand':               item.get('brandName'),
            'product_name':                item.get('productName'),
            'product_reviews_star_rating': item.get('rating'),
            'product_reviews_count':       item.get('reviewCount'),
            'product_price':               item.get('listPrice'),
            'product_sale_price':          sale_price,
        })

    # 5) Build a DataFrame and save it
    df = pd.DataFrame(rows)
    if df.empty:
        print(" No products found in JSON.")
    else:
        df.to_csv("products.csv", index=False)
        print(f" Wrote {len(df)} products to products.csv")

if __name__ == "__main__":
    main()

