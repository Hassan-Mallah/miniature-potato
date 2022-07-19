# import module
from gnewsclient import gnewsclient

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