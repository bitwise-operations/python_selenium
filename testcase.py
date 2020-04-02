import unittest
import page

class TestGoogleSearchIvi(unittest.TestCase):
    """ivi search tests in google"""

    def setUp(self):
        self.g = page.Google_page()

    def tearDown(self):
        self.g.driver_close()

    def test_count_url_the_image_search(self):
        self.assertTrue(self.g.count_url_ivi() > 3)

    def test_rating_matches_on_the_page_and_in_the_search_content(self):
        self.assertEqual(self.g.rating_on_content(), self.g.rating_on_the_page())

    def test_wiki_contain_links_ivi(self):
        self.assertTrue(self.g.search_wiki())

if __name__ == "__main__":
    unittest.main()
