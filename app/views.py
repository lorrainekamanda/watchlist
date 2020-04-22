from flask import render_template,redirect,url_for
from app import app
from .request import get_movies




@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    from .request import get_movies

    # Getting popular movie
    popular_movies = get_movies('popular')
    print(popular_movies)
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title = title,popular = popular_movies)

@app.route('/review')

def overview():
    from .request import get_movies

    popular_movies = get_movies('popular')
    print(popular_movies)
    title = 'welcome to movie reviews'
    return render_template('review.html',title = title,popular = popular_movies)
