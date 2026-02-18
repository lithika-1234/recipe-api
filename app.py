from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)
@app.route("/")
def home():
    return "Recipe API running!"

@app.route("/api/recipes")
def get_recipes():
    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 10))

    offset = (page - 1) * limit

    conn = sqlite3.connect("recipes.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM recipes
    ORDER BY rating DESC
    LIMIT ? OFFSET ?
    """, (limit, offset))

    rows = cursor.fetchall()
    conn.close()

    return jsonify(rows)
@app.route("/api/recipes/search")
def search():
    title = request.args.get("title")
    cuisine = request.args.get("cuisine")

    conn = sqlite3.connect("recipes.db")
    cursor = conn.cursor()

    query = "SELECT * FROM recipes WHERE 1=1"
    params = []

    if title:
        query += " AND title LIKE ?"
        params.append(f"%{title}%")

    if cuisine:
        query += " AND cuisine=?"
        params.append(cuisine)

    cursor.execute(query, params)
    rows = cursor.fetchall()

    conn.close()
    return jsonify(rows)
if __name__ == "__main__":
    app.run(debug=True)

