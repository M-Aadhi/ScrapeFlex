import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'lxml')
        # Example: Extract all paragraphs
        paragraphs = soup.find_all('p')
        return '\n'.join([p.get_text() for p in paragraphs])
    except Exception as e:
        return str(e)
