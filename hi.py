from flask import Flask, render_template, request, redirect, url_for, session
import json
import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

app = Flask(__name__)
app.secret_key = 'supersecretkey'
USERS_FILE = 'users.json'

# ===== USER HANDLING =====
def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, 'r') as file:
        return json.load(file)

def save_users(users):
    with open(USERS_FILE, 'w') as file:
        json.dump(users, file)

# ===== MOVIE DATA =====
MOVIES_FILE = 'movies.csv'

if not os.path.exists(MOVIES_FILE):
    raise FileNotFoundError(f"'{MOVIES_FILE}' not found. Make sure it exists in the same directory as app.py")

movies = pd.read_csv(MOVIES_FILE)  # Ensure this CSV has 'title' and 'description' columns
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['description'].fillna(''))
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
indices = pd.Series(movies.index, index=movies['title']).drop_duplicates()


# ===== ROUTES =====
@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        users = load_users()
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('home'))
        return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        users = load_users()
        username = request.form['username']
        password = request.form['password']
        if username in users:
            return render_template('signup.html', error='Username already exists')
        users[username] = password
        save_users(users)
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    if 'username' not in session:
        return redirect(url_for('login'))

    recommendations = []
    if request.method == 'POST':
        selected_movie = request.form['movie']
        if selected_movie in indices:
            idx = indices[selected_movie]
            sim_scores = list(enumerate(cosine_sim[idx]))
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
            movie_indices = [i[0] for i in sim_scores]
            recommended_titles = movies['title'].iloc[movie_indices]

            # Attach image and IMDb data
            for title in recommended_titles:
                data = movie_posters.get(title, {})
                recommendations.append({
                    "title": title,
                    "image": data.get("image", "https://via.placeholder.com/100"),
                    "imdb": data.get("imdb", "#")
                })

    return render_template(
        'home.html',
        username=session['username'],
        movie_titles=movies['title'].tolist(),
        recommendations=recommendations
    )

if __name__ == '__main__':
    app.run(debug=True)
