# generate_mock_posts.py
# generate_mock_posts.py

import os
import glob
import re
from jinja2 import Environment, FileSystemLoader
from datetime import datetime
from fetch_products import fetch_products_by_category
from generate_ai_review import generate_ai_review

OUTPUT_DIR = 'content'
TEMPLATE_DIR = 'templates'
TEMPLATE_FILE = 'product_post_template.j2'

def slugify(text):
    return re.sub(r'\W+', '-', text.lower()).strip('-')

# Step 0: Clean previous markdown files
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)
else:
    for file_path in glob.glob(os.path.join(OUTPUT_DIR, '*.md')):
        os.remove(file_path)

# Step 1: Fetch products from multiple categories
categories = ["beauty", "smartphones", "laptops", "Sports"]
POSTS_PER_CATEGORY = 2

all_products = []
for category in categories:
    products = fetch_products_by_category(category, count=POSTS_PER_CATEGORY)
    all_products.extend(products)

# Step 2: Add AI reviews and slugs
for product in all_products:
    product['ai_review'] = generate_ai_review(product)
    product['slug'] = slugify(product['title'])
    product['date'] = datetime.now().strftime('%Y-%m-%d')

# Step 3: Setup Jinja2 and render template
env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
template = env.get_template(TEMPLATE_FILE)

for product in all_products:
    output = template.render(product)
    filename = os.path.join(OUTPUT_DIR, f"{product['slug']}.md")
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(output)

print(f"✅ Generated {len(all_products)} product posts in '{OUTPUT_DIR}'.")


'''
import os
from jinja2 import Environment, FileSystemLoader
from fetch_products import fetch_products_by_category # your product fetcher
from generate_ai_review import generate_ai_review  # your AI review function
import re
from datetime import datetime

import os
import glob

OUTPUT_DIR = 'content'

# Step 0: Clean up old markdown files before generating new ones
for file_path in glob.glob(os.path.join(OUTPUT_DIR, '*.md')):
    os.remove(file_path)

# Then continue with your existing code to generate posts...



def slugify(text):
    return re.sub(r'\W+', '-', text.lower()).strip('-')

POST_COUNT = 5

# Step 1: Fetch products
#products = fetch_products_by_category(POST_COUNT)
products = fetch_products_by_category(POST_COUNT)

# Step 2: Add AI reviews, slugs, and dates
for product in products:
    product['ai_review'] = generate_ai_review(product)
    product['slug'] = slugify(product['title'])
    product['date'] = datetime.now().strftime('%Y-%m-%d')

# Step 3: Setup Jinja2 environment
TEMPLATE_DIR = 'templates'
TEMPLATE_FILE = 'product_post_template.j2'
env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
template = env.get_template(TEMPLATE_FILE)

# Step 4: Create output directory
OUTPUT_DIR = 'content'
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Step 5: Render and save each product as Markdown
for product in products:
    output = template.render(product)
    filename = os.path.join(OUTPUT_DIR, f"{product['slug']}.md")
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(output)
        f.write(f'<a href="{product["detail_page_url"]}" target="_blank" style="background:#f90;color:white;padding:10px 15px;border-radius:5px;text-decoration:none;">Buy on Amazon</a>\n\n')

print(f" Generated {POST_COUNT} product posts in '{OUTPUT_DIR}'.")
'''
'''
import os
import re
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
from amazon_fetch import fetch_fakestore_products
from openai_review import generate_ai_review

def slugify(text):
    return re.sub(r'\W+', '-', text.lower()).strip('-')

# Fetch products
POST_COUNT = 5
products = fetch_fakestore_products(POST_COUNT)

# Process each product
for product in products:
    product['ai_review'] = generate_ai_review(product)
    product['slug'] = slugify(product['title'])
    product['date'] = datetime.now().strftime("%Y-%m-%d")

# Jinja2 template setup
TEMPLATE_DIR = 'templates'
TEMPLATE_FILE = 'product_post_template.j2'
env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
template = env.get_template(TEMPLATE_FILE)

# Output folder
OUTPUT_DIR = 'content'
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Render and save
for product in products:
    output = template.render(product)
    filename = os.path.join(OUTPUT_DIR, f"{product['slug']}.md")
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(output)

print(f"✅ Generated {POST_COUNT} product posts in '{OUTPUT_DIR}'.")
'''
'''
import os
from jinja2 import Environment, FileSystemLoader  # ✅ Correct
from amazon_fetch import fetch_fakestore_products  # ✅ Updated to use real data

# Fetch products
POST_COUNT = 5
products = fetch_fakestore_products(POST_COUNT)

# Jinja2 template setup
TEMPLATE_DIR = 'templates'
TEMPLATE_FILE = 'product_post_template.j2'
env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
template = env.get_template(TEMPLATE_FILE)

# Output folder
OUTPUT_DIR = 'content'
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Render and save
for product in products:
    output = template.render(product)
    filename = os.path.join(OUTPUT_DIR, f"{product['slug']}.md")
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(output)

from openai_review import generate_ai_review

# inside your loop:
for product in products:
    product['ai_review'] = generate_ai_review(product)
    output = template.render(product)
    ...

print(f"✅ Generated {POST_COUNT} product posts in '{OUTPUT_DIR}'.")

'''