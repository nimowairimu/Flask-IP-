from flask import render_template
from app import app
from .request import get_articles, get_sources

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    politics  = get_articles('politics ')
    


