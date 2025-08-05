# generate_ai_review.py

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

def generate_ai_review(product):
    if not api_key:
        return f"(Placeholder) This is a sample review for {product['title']}."

    client = OpenAI(api_key=api_key)

    prompt = (
        f"Write a compelling, SEO-friendly product review for the following product:\n"
        f"Title: {product['title']}\n"
        f"Description: {product['summary']}\n"
        f"Price: {product['price']}\n"
    )

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a product review assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=300
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error generating review: {e}"
