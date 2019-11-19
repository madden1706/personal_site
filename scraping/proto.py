from bs4 import BeautifulSoup, SoupStrainer
import requests
import re
import datetime


headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get('https://old.reddit.com/r/ukpolitics', headers=headers)

siteTable = SoupStrainer(id="siteTable")

soup = BeautifulSoup(r.text, 'html.parser', parse_only=siteTable)
print(soup.prettify())


links = soup.find_all('a', 'bylink comments may-blank')

#print(links)
for i in links:
    sub_link = i.get('href')
    print(i)

print("=======")
ids = soup.find_all('div', re.compile("^thing id-t3_.*"))

# dask 

for i in ids:

    # make a dict: 
    print("----")
    #i.prettify()

    print(i.get('data-fullname'))
    print(i.get('data-author'))
    print(i.get('data-comments-count'))
    print(i.get('data-promoted'))
    print(i.get('data-timestamp'))
    likes = i.find_all('div', 'score likes')
    print(likes[0].get('title'))
    dislikes = i.find_all('div', 'score dislikes')
    print(dislikes[0].get('title'))
    # time is in milliseconds
    readable = datetime.datetime.fromtimestamp(int(i.get('data-timestamp'))/1000).isoformat()
    print(readable)
    print("----")

    


