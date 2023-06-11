import requests

r=requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=3e37587c0af2439a8dfe5a0e6fc7c9ca')

content=r.json()

print(content)

print(content['articles'][0]['title'])

articles=content['articles']

for article in articles:
    print(article['title'])

#Write a function that gets the news titles and its description and stores them in a python list

def get_news(topic, from_date, to_date, language='en',
            api_key='3e37587c0af2439a8dfe5a0e6fc7c9ca'):
  url = f'https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}8&sortBy=popularity&language={language}&apiKey={api_key}'
  r = requests.get(url)
  content = r.json()
  articles = content['articles']
  results = []
  for article in articles:
    results.append(f"TITLE\n'{article['title']}, '\nDESCRIPTION\n', {article['description']}")
  return results

print(get_news(topic='space', from_date='2022-11-25', to_date='2022-11-28'))




