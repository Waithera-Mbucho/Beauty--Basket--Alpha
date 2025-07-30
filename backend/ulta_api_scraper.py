import requests, pandas as pd

# Paste the URL you copied between the quotes:
url = "https://www.ulta.com/dxl/graphql?ultasite=en-us&user-agent=gomez&query=query%20NonCachedPage(%24stagingHost%3A%20String%2C%20%24previewOptions%3A%20JSON%2C%20%24moduleParams%3A%20JSON%2C%20%24url%3A%20JSON)%20%7B%0A%20%20Page%3A%20NonCachedPage(stagingHost%3A%20%24stagingHost%2C%20previewOptions%3A%20%24previewOptions%2C%20moduleParams%3A%20%24moduleParams%2C%20url%3A%20%24url%2C%20contentId%3A%20%22f721ee29-2956-4447-a91b-8298e6dabae6%22%2C%20echoParams%3A%20%7BcategoryKeys%3A%20%22c10263%22%7D)%20%7B%0A%20%20%20%20content%0A%20%20%20%20customResponseAttributes%0A%20%20%20%20meta%0A%20%20%20%20__typename%0A%20%20%7D%0A%7D%0A&operationName=NonCachedPage&variables=%7B%22moduleParams%22%3A%7B%22gti%22%3A%22936c0e1b-1742-4d3d-9a6e-66b5e0eee1f0%22%2C%22loginStatus%22%3A%22anonymous%22%7D%7D"

resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
data = resp.json()

# Extract names/prices
products = []
for p in data["products"]:
    products.append({
        "name":  p["displayName"],   # ← comma here
        "price": p["listPrice"]      # ← then close the dict
    })

df = pd.DataFrame(products)
print(df)

