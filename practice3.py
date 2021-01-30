import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
votes = soup.select('.score')


def create_custom_hn(links, votes):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        points = int(votes[idx].getText().replace(' points', ''))
        print(points)
        hn.append({'title': title, 'link': href})
    return hn


create_custom_hn(links, votes)
# print(create_custom_hn(links, votes))


