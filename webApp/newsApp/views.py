from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from gnewsclient import gnewsclient


# Create your views here.

def news(request: HttpRequest):
    # declare a NewsClient object
    client = gnewsclient.NewsClient(
        language='english',
        location='turkey',
        topic='Business',
        max_results=5)

    # get news feed
    news = client.get_news()

    for item in news:
        print("Title : ", item['title'])
        print("Link : ", item['link'])
        print("")

    # in html file, you use key names directly :)
    context = {
        # "news": "This is news view"
        "news": news
    }
    return render(request, 'news.html', context=context)
