#  Movie Recommendation System

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-Flask-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An end-to-end Machine Learning web application that recommends movies based on user preferences and content similarity. Built with Python, Flask, and an interactive frontend template.

---

##  Project Overview
The *Movie Recommendation System* processes movie metadata to calculate similarity scores between titles and suggests top relevant recommendations to the user in real-time. It features a clean web UI powered by Flask and HTML/CSS templates.

---

##  Key Features
- *Smart Recommendations:* Uses Machine Learning algorithms to compute movie similarity.
- *Interactive Web Interface:* User-friendly UI built using Flask templates and static assets.
- *Fast Search & Processing:* Efficient data handling using Pandas and NumPy.
- *Data Visualizations:* In-depth exploratory analysis included in the Jupyter Notebook.

---

##  Tech Stack & Tools

- *Programming Language:* Python
- *Web Framework:* Flask
- *Data Science Libraries:* Pandas, NumPy, Scikit-learn
- *Frontend:* HTML5, CSS3, JavaScript
- *Development Environment:* Jupyter Notebook, VS Code

---

##  Project Structure

```text
Movie_recommendation_system/
├── static/                 # CSS, JavaScript, and image assets
├── templates/              # HTML templates (e.g., index.html)
├── app.py                  # Main Flask application
├── moviesproject.ipynb     # Machine Learning notebook & EDA
├── movies.csv              # Movie dataset
├── user.json               # Configuration/User data
├── README.md               # Project documentation
└── .gitignore              # Ignored system files
