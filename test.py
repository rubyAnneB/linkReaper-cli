"""This is the file that contains all of the tests for LinkReaper"""
import unittest
import linkReaper


class TestLinkReaper(unittest.TestCase):
    """Test Class for LinkReaper"""

    def test_get_website_response(self):
        """Test to make sure that you are able to get the response from a website"""
        res = linkReaper.getwebsiteresponse("https://urllib3.readthedocs.io/en/latest/reference/"
                                            "urllib3.poolmanager.html")
        self.assertIsNot(res, None)

    def test_get_website_response_none(self):
        """Test to make sure that you are able to get the response from a website"""
        res = linkReaper.getwebsiteresponse("")
        self.assertIs(res, None)

    def test_collect_links_none(self):
        """Make sure that the function is able to read and retrieve links"""
        links = None
        with open("index2.html", "r") as file:
            links = linkReaper.collect_links(file.read(), False)

        self.assertIsNot(links, None)

    def test_collect_links_valid(self):
        """checks that the scheme is there"""
        links = None
        with open("index2.html", "r") as file:
            links = linkReaper.collect_links(file.read(), False)

        valid = False

        for link in links:
            if "http" in link:
                valid = True

        self.assertIs(valid, True)



if __name__ == '__main__':
    unittest.main()
