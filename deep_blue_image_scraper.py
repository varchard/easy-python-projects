import requests
import bs4
temp_store = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')
deep_blue = bs4.BeautifulSoup(temp_store.text,'lxml')
images = deep_blue.select('.thumbimage')
image_urls = []
for item in images:
    image_urls.append('https:' + item['src'])
count = 1
for item in image_urls:
    f = open(f'computer_image{count}.jpg','wb')
    f.write(requests.get(item).content)
    f.close
    count += 1