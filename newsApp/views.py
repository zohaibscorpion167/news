from django.shortcuts import render
import requests
import json 
# Create your views here.

API_KEY= 'f6462f809cee4297b73bb564cfc18e59'

def index(request):
    country = 'us'
    num_news = '20'
    category = 'general'
    news_api_request = requests.get('http://newsapi.org/v2/top-headlines?country='+country+'&pageSize='+num_news+'&category='+category+'&apiKey='+API_KEY)
    news_api_all = json.loads(news_api_request.content)

    country = 'us'
    num_news = '5'
    category = 'sports'
    news_api_request_sports = requests.get('http://newsapi.org/v2/top-headlines?country='+country+'&pageSize='+num_news+'&category='+category+'&apiKey='+API_KEY)
    news_api_sports = json.loads(news_api_request_sports.content)


    country = 'us'
    num_news = '6'
    category = 'business'
    news_api_request_business = requests.get('http://newsapi.org/v2/top-headlines?country='+country+'&pageSize='+num_news+'&category='+category+'&apiKey='+API_KEY)
    news_api_business = json.loads(news_api_request_business.content)


    query = 'bitcoin'
    num_news = '1'
    news_api_request_bitcoin = requests.get('http://newsapi.org/v2/everything?q='+query+'&pageSize='+num_news+'&excludeDomains=google.com'+'&apiKey='+API_KEY)
    news_api_bitcoin = json.loads(news_api_request_bitcoin.content)


    return render(request, 'index.html', {'news_api_all': news_api_all, 'news_api_sports': news_api_sports, 'news_api_business' : news_api_business, 'news_api_bitcoin': news_api_bitcoin})



def search_news(request):
    if request.method == "POST":
        fromdate = request.POST.get('from')
        todate = request.POST.get('to')
        query = request.POST.get('query')
        num_news = '15'
        news_api_request_date = requests.get('http://newsapi.org/v2/everything?q='+query+'&from='+fromdate+'&to='+todate+'&pageSize='+num_news+'&excludeDomains=google.com'+'&apiKey='+API_KEY)
        news_api_request_date = json.loads(news_api_request_date.content)
        return render(request, 'search.html', {'news_api_request_date' : news_api_request_date})
    return render(request, 'search.html')
    