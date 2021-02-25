import os

class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL =os.environ.get('https://newsapi.org/v2/sources?language=en&category={}&apiKey={}')
    NEWS_ARTICLES_URL =os.environ.get('https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}')
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')


class ProdConfig(Config):
     pass

class DevConfig(Config):

    DEBUG = True



config_options = {
'development':DevConfig,
'production':ProdConfig
}