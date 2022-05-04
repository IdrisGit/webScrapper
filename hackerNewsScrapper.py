import requests
from bs4 import BeautifulSoup
import pprint

#To Sort in Decending Order Of Votes
def sort_stories_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)

#Create Custom List With Votes Over 100
def custom_hn(links, subtext):
    hn = []
    for i, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        votes = subtext[i].select('.score')
        if len(votes):
            points = int(votes[0].getText().replace('points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_votes(hn)


def pages(i):
    #For 1st Page Only
    url = 'https://news.ycombinator.com/news'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    links = soup.select(".titlelink")
    subtext = soup.select(".subtext")

    #For More Pages
    for page in range(i):
        res2 = requests.get('https://news.ycombinator.com/news?p=' + str(page))
        soup2 = BeautifulSoup(res2.text, 'html.parser')
        links2 = soup2.select(".titlelink")
        subtexts2 = soup2.select(".subtext")
    mega_link = links + links2
    mega_subtext = subtext + subtexts2
    pprint.pprint(custom_hn(mega_link, mega_subtext))


pages(int(input('No. of pages')))
