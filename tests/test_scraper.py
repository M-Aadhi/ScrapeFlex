import unittest
from scrape_flex.scraper import scrape_website

class TestScraper(unittest.TestCase):
    def test_scrape_website(self):
        # You can add real URLs and expected results here
        url = 'https://example.com'
        result = scrape_website(url)
        self.assertIn('Example Domain', result)

if __name__ == '__main__':
    unittest.main()
