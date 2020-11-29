"""This is the file that contains all of the tests for LinkReaper"""
import unittest
import io
import linkReaper


class TestLinkReaper(unittest.TestCase):
    """Test Class for LinkReaper"""

    def test_get_website_response(self):
        """Test to make sure that you are able to get the
        response from a website"""
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

        valid = True
        last = False
        while valid and not last:
            for link in links:
                if "http" not in link:
                    valid = False
                    print(link)

                # break out of the loop
                if link is links[-1]:
                    last = True

        self.assertIs(valid, True)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_output_codes(self, links, expected_output, mock_stdout=None):
        """tests the output of the output_codes function"""
        linkReaper.output_codes(links)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_outout_codes(self):
        """tests that you are getting the proper printing from the
        website"""
        links = ["www.google.com"]
        self.assert_output_codes(links, "GOOD      - Successful  : 200 www.google.com\n")


if __name__ == '__main__':
    unittest.main()
