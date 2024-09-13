import requests as rq
import json
query = input("Enter you chooice  News? = ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-08-13&sortBy=publishedAt&apiKey=d010b3457d8647cea8533e96240fdd58"
r = rq.get(url)
news = json.loads(r.text)

for artical in news["articles"]:
    print(artical["title"])
    print(artical["description"])
    print("-----------------------------------")