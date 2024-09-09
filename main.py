from bs4 import BeautifulSoup
import requests

response=requests.get("https://news.ycombinator.com/")


soup=BeautifulSoup(response.text,"html.parser")
articles=soup.select(selector=".titleline a")
articles_text=[]
articles_links=[]
for article in articles:
    text=article.getText()
    articles_text.append(text)

# article_upvotes=soup.find(name="span",class_="score").getText()
print(articles_text)