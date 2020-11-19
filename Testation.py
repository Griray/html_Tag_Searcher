import unittest
from main import searcher, link


class TestSearcher(unittest.TestCase):
    def setUp(self):
        print('method setUp')

    def tearDown(self):
        print('method tearDown')

    def test_get_html(self):
        self.assertEqual(searcher.get_html_for_test(link), '<Response [200]>')



if __name__ == "__main__":
    unittest.main()
