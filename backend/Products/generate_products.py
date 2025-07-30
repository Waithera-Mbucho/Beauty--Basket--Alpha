
import json
import pandas as pd
import os
import sys

# ————————————————————————————————
# Configuration: change these if needed
INPUT_BASENAME  = "products"       # your JSON file, without extension
OUTPUT_BASENAME = "products"       # desired CSV filename, without extension
# ————————————————————————————————


def main():
    # Determine filenames
    input_file = INPUT_BASENAME
    if not os.path.splitext(input_file)[1]:
        input_file += ".json"

    output_file = OUTPUT_BASENAME
    if not os.path.splitext(output_file)[1]:
        output_file += ".csv"

    # Load the JSON
    with open(input_file, 'r') as f:
        data = json.load(f)

    # Drill down to the list of items
    items = data.get('data', {}) \
                .get('Page', {}) \
                .get('content', {}) \
                .get('items', [])

    # Extract into rows
    rows = []
    for item in items:
        rows.append({
            'product_brand':              item.get('brandName'),
            'product_name':               item.get('productName'),
            'product_reviews_star_rating':item.get('rating'),
            'product_reviews_count':      item.get('reviewCount'),
            'product_price':              item.get('listPrice'),
            'product_sale_price':         item.get('salePrice') or item.get('listPrice'),
        })

    # Build DataFrame and write CSV
    df = pd.DataFrame(rows)
    df.to_csv(output_file, index=False)
    print(f"✅ Wrote {len(df)} rows to {output_file}")


if __name__ == "__main__":
    main()
