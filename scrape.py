import requests
from bs4 import BeautifulSoup
import pprint

pages = int(input("How many pages of Hacker News do you want: "))


def request_hn(pages):
    mega_links = []
    mega_subtext = []
    for page in range(1, pages+1):
        res = requests.get('https://news.ycombinator.com/news?p='+str(page))
        soup = BeautifulSoup(res.text, 'html.parser')
        links = soup.select('.storylink')
        subtext = soup.select('.subtext')
        mega_links += links
        mega_subtext += subtext
    return mega_links, mega_subtext


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


def create_file(output):
    filename = f'{pages}_pages_of_top_Hacker_news_articles.txt'
    with open(filename, mode='a') as my_file:
        for page in output:
            for key, value in page.items():
                my_file.write(str(key)+": "+str(value)+'\n')
            my_file.write("------------------------------"+'\n')


links, subtext = request_hn(pages)
output = create_custom_hn(links, subtext)
create_file(output)
