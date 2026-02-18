import json
import sqlite3

with open("US_recipes_null.json") as f:
    data = json.load(f)

recipes = list(data.values())

conn = sqlite3.connect("recipes.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS recipes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cuisine TEXT,
    title TEXT,
    rating REAL,
    prep_time INTEGER,
    cook_time INTEGER,
    total_time INTEGER,
    description TEXT,
    nutrients TEXT,
    serves TEXT
)
""")

for r in recipes:
    cursor.execute("""
    INSERT INTO recipes
    (cuisine, title, rating, prep_time, cook_time,
     total_time, description, nutrients, serves)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        r.get("cuisine"),
        r.get("title"),
        r.get("rating"),
        r.get("prep_time"),
        r.get("cook_time"),
        r.get("total_time"),
        r.get("description"),
        json.dumps(r.get("nutrients")),
        r.get("serves")
    ))

conn.commit()
conn.close()

print("Database created and data inserted!")
