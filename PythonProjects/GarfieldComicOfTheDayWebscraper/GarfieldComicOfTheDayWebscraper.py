#! python3

from bs4 import BeautifulSoup
import twitter
import requests

authenticate = 'https://garfield.com/agegate'
comic = 'https://garfield.com/comic'

def tokenScrape():
  with requests.session() as s:
    r = s.get(comic)
    # Scrape the main website
    soup  = BeautifulSoup(r.content, 'html.parser')
    # Find the website token
    token = soup.find('input', {'name': '_token'})['value']

    # Answer the token question to be 'adult' for the Garfield themed anti-bot question
    # Discard First Response:
    # The POST must be sent twice for this site so discard the first
    # http://docs.python-requests.org/en/master/user/quickstart/
    s.post(authenticate, data={'_token': token, 'role': 'adult'})

    # Answer the question a second time:
    r = s.post(authenticate, data={'_token': token, 'role': 'adult'})
    soup = BeautifulSoup(r.text, 'html.parser')

    return soup

def comicScrape(soup):
  # print('soup = ' + str(soup))
  images = soup.findAll('img', class_='img-responsive')
  garfieldComicMatch = images[0]
  # print('garfieldComicMatch = ' + str(garfieldComicMatch))
  garfieldComicMatchLink = images[0]['src']
  # print('garfieldComicMatchLink = ' + str(garfieldComicMatchLink))
  return garfieldComicMatchLink

def postToTwitter(garfieldComicMatchLink):
  # print('garfieldComicMatchLink = ' + str(garfieldComicMatchLink))
  api = twitter.Api(
    # NOTE: You must provide your OWN Twitter Developer API keys to post on your Twitter account:
    consumer_key="",
    consumer_secret="",
    access_token_key="",
    access_token_secret=""
  )

  status = api.PostUpdate('Here Is The Garfield Comic of The Day!\n\nThe Comic Can Be Found Here:\n' + garfieldComicMatchLink, media=garfieldComicMatchLink)

soup = tokenScrape()
garfieldComicMatchLink = comicScrape(soup)
postToTwitter(garfieldComicMatchLink)
