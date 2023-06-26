import requests
from bs4 import BeautifulSoup as bs

res = requests.get('https://news.ycombinator.com/news')

soup = bs(res.text, 'html.parser')

article_texts = []
article_links = []

for i in soup.find_all('a', class_='titleline'):
    print(i.findChildren())

article_upvotes = [upvote.text.split(' ')[0] for upvote in soup.select(selector='.score')]

# for i in range(10):
    # print(article_texts[i], article_links[i], article_upvotes[i])

max_upvote_value = 0 
max_upvote_index = 0
for upvote, index in enumerate(article_upvotes):
    if upvote > max_upvote_value:
        max_upvote_value = upvote
        max_upvote_index = index

max_upvote_index = int(max_upvote_index)
print(max_upvote_index, len(article_texts))

most_popular_article = {
    'text': article_texts[max_upvote_index],
    'links': article_links[max_upvote_index],
    'upvotes': max_upvote_value
}

print(most_popular_article)


