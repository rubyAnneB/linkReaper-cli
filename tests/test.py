"""This is the file that contains all of the tests for LinkReaper"""
import unittest
from unittest import mock  # pylint: disable=unused-import
import io
import os
import linkReaper


# click has its own testing capabilities- add some of these in
#  use click.test for testing the commands directly-
# is there some way to integrate it with unnittest?

TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), "testdata.html")


class TestLinkReaper(unittest.TestCase):
    """Test Class for LinkReaper"""

    def test_get_website_response_none(self):
        """Test to make sure that you are able to get the response from a website"""
        res = linkReaper.getwebsiteresponse("")
        self.assertIs(res, None)

    def test_collect_links_none(self):
        """Make sure that the function is able to read and retrieve links"""
        links = None
        with open(TESTDATA_FILENAME, "r") as file:
            links = linkReaper.collect_links(file.read(), False)

        self.assertIsNot(links, None)

    def test_collect_links_valid(self):
        """checks that the scheme is there"""
        links = None
        with open(TESTDATA_FILENAME, "r") as file:
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

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def assert_output_codes(self, links, expected_output, mock_stdout=None):
        """tests the output of the output_codes function"""
        linkReaper.output_codes(links)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    @unittest.mock.patch("linkReaper.urllib3.PoolManager.request")
    def get_website_response_good(self, mock_request=None, mock_stdout=None):
        """gets mock httpresponses"""
        mock_request.return_value.status = 200
        url = ["www.goodwebsite.com"]
        linkReaper.output_codes(url)
        self.assertEqual(
            mock_stdout.getvalue(),
            "GOOD      - Successful  " ": 200 www.goodwebsite.com\n",
        )

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    @unittest.mock.patch("linkReaper.urllib3.PoolManager.request")
    def get_website_response_good_paramtrue(self, mock_request=None, mock_stdout=None):
        """gets mock httpresponses"""
        mock_request.return_value.status = 200
        url = ["www.goodwebsite.com"]
        linkReaper.output_codes(url, good_links=True)
        self.assertEqual(
            mock_stdout.getvalue(),
            "GOOD      - Successful  " ": 200 www.goodwebsite.com\n",
        )

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    @unittest.mock.patch("linkReaper.urllib3.PoolManager.request")
    def get_website_response_good_paramfalse(self, mock_request=None, mock_stdout=None):
        """gets mock httpresponses"""
        mock_request.return_value.status = 200
        url = ["www.goodwebsite.com"]
        linkReaper.output_codes(url, bad_links=True)
        self.assertEqual(mock_stdout.getvalue(), "")

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    @unittest.mock.patch("linkReaper.urllib3.PoolManager.request")
    def get_website_response_bad(self, mock_request=None, mock_stdout=None):
        """gets mock httpresponses"""
        mock_request.return_value.status = 400
        url = ["www.badwebsite.com"]
        linkReaper.output_codes(url)
        self.assertEqual(
            mock_stdout.getvalue(),
            "BAD       - Client Error" ": 400 www.badwebsite.com\n",
        )

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    @unittest.mock.patch("linkReaper.urllib3.PoolManager.request")
    def get_website_response_bad_paramtrue(self, mock_request=None, mock_stdout=None):
        """gets mock httpresponses"""
        mock_request.return_value.status = 400
        url = ["www.badwebsite.com"]
        linkReaper.output_codes(url, bad_links=True)
        self.assertEqual(
            mock_stdout.getvalue(),
            "BAD       - Client Error" ": 400 www.badwebsite.com\n",
        )

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    @unittest.mock.patch("linkReaper.urllib3.PoolManager.request")
    def get_website_response_bad_paramfalse(self, mock_request=None, mock_stdout=None):
        """gets mock httpresponses"""
        mock_request.return_value.status = 400
        url = ["www.badwebsite.com"]
        linkReaper.output_codes(url, good_links=True)
        self.assertEqual(mock_stdout.getvalue(), "")

    def test_website_response_good(self):
        """test for good and bad website responses"""
        self.get_website_response_good()
        self.get_website_response_good_paramtrue()
        self.get_website_response_good_paramfalse()

        self.get_website_response_bad()
        self.get_website_response_good_paramtrue()
        self.get_website_response_bad_paramfalse()


if __name__ == "__main__":
    unittest.main()
