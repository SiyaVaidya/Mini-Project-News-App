import requests
from datetime import date

query=input("What type of News are you interested in today ?\n")
api=""  # Add your NewsAPI key here 
today = date.today().strftime("%Y-%m-%d")

url=f"https://newsapi.org/v2/everything?q={query}&from={today}&sortBy=publishedAt&apiKey={api}"

r= requests.get(url)
data = r.json()

articles = data["articles"]

for index, article in enumerate(articles):
    print(index+1,article["title"])
    print(article["url"])
    print("\n**************************************\n")
