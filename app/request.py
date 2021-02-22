import urllib.request,json
from .models import Articles,Sources
import os


api_key = None
base_url = None
artocles_url = None

def configure_request(app):
    global api_key,base_url,articles_url
     api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    articles_url = app.config['NEWS_ARTICLES_URL']


def get_sources(category):
    """
    function that gets response from the api call
    """    
    get_sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

         sources_results = None

         if get_sources_response['sources']:
            sources_results_list = get_news_sources_response['sources']
            sources_results = process_results(sources_results_list)
    return sources_results

def process_ressults(sources_list):
    sources_results = []

    for source in sources_list:
        id = source.get("id")
        name = source.get("name")
        description = source.get("description")
        url = source.get("url")
        category = source.get("category")
        country = one_source.get("country")
        
        source_object = Sources(id,name,description,url,category,country)
        sources_results.append(source_object)
    
    return sources_results 

def get_articles(id):
    '''
    Function that processes the articles and returns a list of articles objects
    '''

    get_articles_url = articles_url.format(id,api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_response = json.loads(url.read())
        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(new_articles_results_list)
    return articles_results

def process_articles(articles_list):
    articles_results = []

    for article in articles_list:
        id = article.get("id")
        author = article.get("author")
        description = article.get("description")
        title = article.get("title")
        url = article.get("url")
        urlToImage = article.get("urlToImage")
        publishedAt = article.get("publishedAt") 

        if urlToImage:
            articles_object = Articles(id,author,title,description,url,urlToImage,publishedAt)
            articles_results.append(news_articles_object)  
    return articles_results
    









