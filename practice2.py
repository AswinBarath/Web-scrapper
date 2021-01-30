import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')

soup = BeautifulSoup(res.text, 'html.parser')

# BeautifulSoup Selectors
# print(soup.select('a'))
# print(soup.select('div'))

print(soup.select('.score'))
# print(soup.select('#score_20514755'))

# print(soup.select('.storylink'))
# print(soup.select('.storylink')[0])


# links = soup.select('.storylink')
# votes = soup.select('.score')
# print(votes)
# print(votes[0].get('id'))


