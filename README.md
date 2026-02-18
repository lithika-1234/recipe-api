# Recipe API Integration Project

## Overview
This project demonstrates backend API development and data integration using Python, Flask, and SQLite. 
Recipe data from a JSON dataset is parsed, stored in a database, and exposed through RESTful APIs that 
support pagination, search, and record counting.

The project showcases API integration, database operations, and modular backend design.

---

## Features
- Parse recipe dataset from JSON
- Store structured data in SQLite database
- REST API built with Flask
- Pagination using limit and offset
- Search recipes by title and cuisine
- Retrieve total record count
- Modular backend implementation

---

## Tech Stack
Python  
Flask  
SQLite  
JSON  

---
Recipe_api/
│
├── app.py
├── setup_db.py
├── US_recipes_null.json
├── recipes.db
└── README.md


---

## API Endpoints

Get recipes (paginated)


GET /api/recipes?page=1&limit=10


Search recipes


GET /api/recipes/search?title=pie
GET /api/recipes/search?cuisine=Southern Recipes


Get record count


GET /api/recipes/count


---

## How to Run

Install dependencies:


pip install flask


Load data into database:


python setup_db.py


Run API server:


python app.py


Server runs at:


http://127.0.0.1:5000


---

## Learning Outcomes
- JSON parsing in Python
- SQLite database integration
- REST API development with Flask
- Pagination implementation
- Dynamic SQL query building
- Backend API integration workflow


After pasting it into README.md, just run:

git add README.md
git commit -m "Added README"
git push

## Project Structure
