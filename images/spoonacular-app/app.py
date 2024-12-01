from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

SPOONACULAR_API_KEY = os.getenv('SPOONACULAR_API_KEY')

@app.route('/', methods=['GET'])
def get_recipe():
    ingredients = request.args.get('ingredients')
    if not ingredients:
        return jsonify({"error": "Please provide ingredients"}), 400

    url = f"https://api.spoonacular.com/recipes/findByIngredients"
    params = {
        "ingredients": ingredients,
        "apiKey": SPOONACULAR_API_KEY,
    }

    response = requests.get(url, params=params)
    recipes = response.json()
    title = []
    
    for recipe in recipes:
        title.append(recipe['title'])
    if response.status_code == 200:
        return jsonify({"suggestions": title})
    else:
        return jsonify({"error": response.text}), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
