import requests
import bs4
data = requests.get('http://quotes.toscrape.com/')
soup = bs4.BeautifulSoup(data.text, 'lxml')
# extract information about authors on page one stored in list authors
authors = (soup.select('.author'))
listauthors = []
for author in authors:
    listauthors.extend(author.contents)
print(listauthors)
# extract quotes, stored in list quotes
listquotes = []
quotes = soup.select('.text')
for quote in quotes:
    listquotes.extend(quote.contents)
print(listquotes)
# extract most popular tags from homepage, stored in listtags
listtags = []
tags = soup.select('.tag-item')
for tag in tags:
    listtags.extend(tag.find('a').contents)
#the code below crawls all the pages of the website to extract the authors
url = 'http://quotes.toscrape.com/page/{}/'
listauthors = []
soup = bs4.BeautifulSoup(requests.get('http://quotes.toscrape.com/').text, 'lxml')
authors = (soup.select('.author'))
for author in authors:
    listauthors.extend(author.contents)
for page in range(2,15):
    if requests.get(url.format(page)).status_code != 200:
        break
    else:
        soup = bs4.BeautifulSoup(requests.get(url.format(page)).text, 'lxml')
        authors = (soup.select('.author'))
        for author in authors:
            listauthors.extend(author.contents)
print(listauthors)

#whoops, instructions actually wanted a list of unique authors
#here I have used properties of a set to accomplish this
url = 'http://quotes.toscrape.com/page/{}/'
listauthors = set()
soup = bs4.BeautifulSoup(requests.get('http://quotes.toscrape.com/').text, 'lxml')
authors = (soup.select('.author'))
for author in authors:
    listauthors.add(author.text)
for page in range(2,15):
    if requests.get(url.format(page)).status_code != 200:
        break
    else:
        soup = bs4.BeautifulSoup(requests.get(url.format(page)).text, 'lxml')
        authors = (soup.select('.author'))
        for author in authors:
            listauthors.add(author.text)
print(listauthors)