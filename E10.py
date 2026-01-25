import requests

API_KEY = "  "   
URL = "https://newsapi.org/v2/top-headlines"

topics = ["technology", "sports", "business", "health", "entertainment"]

for topic in topics:

    print(f"\n  {topic.upper()} NEWS\n")

    params = {
        "apiKey": API_KEY,
        "category": topic,
        "country": "pk",
        "pageSize": 5
    }

    response = requests.get(URL, params=params)
    data = response.json()

    if data["status"] == "ok":
        for i, article in enumerate(data["articles"], start=1):
            print(f"{i}. {article['title']}")
    else:
        print("Error fetching news!")
