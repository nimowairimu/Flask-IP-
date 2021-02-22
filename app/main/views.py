from flask import render_template,redirect,request,url_for
from . import main
from ..models imort Sources
from ..request import get_sources,get_articles

@main.route('/')
def Index():
    """
   Function that returns the index page and the data it contains 
    """
    general_news = get_sources('general')
    business_news = get_sources("business")
    sports_news = get_sources("sports")
    entertainment_news = get_articles("entertainment")

    return render_template('index.html',general=general_news,business=business_news,sports=sports_news,entertainment=entertainment_news)
    
    title='Homepage'

@main.route('/articles/<id>')
def articles(id):
    '''
    Function to view articles page
    '''
    news_articles = get_articles(id)
    title =f'{id}'
    return render_template('articles.html',title=title, articles='news_articles')
