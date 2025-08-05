# fetch_products.py
# fetch_products.py

from datetime import datetime
import requests

AFFILIATE_TAG = "kenenitech-20"

def generate_affiliate_link(product_title):
    base_url = "https://www.amazon.com/s?k="
    search_query = product_title.replace(" ", "+")
    return f"{base_url}{search_query}&tag={AFFILIATE_TAG}"

def fetch_products_by_category(category, count=5):
    url = f"https://dummyjson.com/products/category/{category}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()

    products = data['products'][:count]

    cleaned_products = []
    for product in products:
        cleaned_products.append({
            "title": product.get("title"),
            "price": f"${product.get('price')}",
            "summary": product.get("description"),
            "image_url": product.get("images")[0] if product.get("images") else "",
            "detail_page_url": generate_affiliate_link(product.get("title")),
            "date": datetime.now().strftime("%Y-%m-%d"),
            "category": category.capitalize(),
            "tags": ", ".join(product.get("tags", [])) if product.get("tags") else f"{category}, affiliate",
            "features": product.get("features", []),
            "ai_review": "AI-generated review goes here..."  # Placeholder
        })
    return cleaned_products


'''
from datetime import datetime
import requests

AFFILIATE_TAG = "kenenitech-20"

def generate_affiliate_link(product_title):
    base_url = "https://www.amazon.com/s?k="
    search_query = product_title.replace(" ", "+")
    return f"{base_url}{search_query}&tag={AFFILIATE_TAG}"

def fetch_products_by_category(category, count=5):
    url = f"https://dummyjson.com/products/category/{category}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()

    products = data['products'][:count]

    cleaned_products = []
    for product in products:
        cleaned_products.append({
            "title": product.get("title"),
            "price": f"${product.get('price')}",
            "summary": product.get("description"),
            "image_url": product.get("images")[0] if product.get("images") else "",
            "detail_page_url": generate_affiliate_link(product.get("title")),
            "date": datetime.now().strftime("%Y-%m-%d"),
            "category": category,
            "tags": ", ".join(product.get("tags", [])) if product.get("tags") else f"{category}, affiliate",
            "features": product.get("features", []),
            "ai_review": "AI-generated review goes here..."
        })
    return cleaned_products

if __name__ == "__main__":
    categories = ["beauty", "smartphones", "laptops"]  # Add more as needed
    all_products = []

    for category in categories:
        products = fetch_products_by_category(category, count=3)
        all_products.extend(products)

    for p in all_products:
        print(f"Title: {p['title']}")
        print(f"Price: {p['price']}")
        print(f"Category: {p['category']}")
        print(f"Image URL: {p['image_url']}")
        print(f"Affiliate URL: {p['detail_page_url']}")
        print(f"Summary: {p['summary']}")
        print("-" * 40)
'''
'''
import requests

def fetch_products(count=5):
    url = "https://dummyjson.com/products"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
    return data['products'][:count]

if __name__ == "__main__":
    products = fetch_products(3)
    for p in products:
        print(p['title'], p['price'])
'''