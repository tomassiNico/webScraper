from bs4 import BeautifulSoup
import requests

INFOBAE_URL = 'https://www.infobae.com/'

def get_beautiful_soup(url):
    re = requests.get(url)
    if re.status_code == 200:
        return BeautifulSoup(re.text, 'html.parser')

def scraping_site():

    soup = get_beautiful_soup(INFOBAE_URL)

    if soup is not None:
        articles = soup.find_all('div', {'class':'headline normal normal-style'})
        for article in articles:
            title = article.find('a').getText()
            url = INFOBAE_URL+article.find('a').get('href')
            subdata = get_beautiful_soup(url)
            subtitulo = subdata.find('span',{'class':'subheadline'}).getText()

            print('Titulo: {} \nResumen: {} \nLink: {}\n'.format(title,subtitulo,url))

if __name__ == '__main__':
    scraping_site()

