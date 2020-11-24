import unittest
from unittest.mock import patch
from searcher import TagSearcher


class TestSearcher(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        self.link1 = TagSearcher('https://www.google.com')
        self.link2 = TagSearcher('https://www.vk.com')
        print('method setUp')

    def tearDown(self):
        print('method tearDown')

    def test_get_html(self):
        with patch('searcher.TagSearcher.get_html') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            result = self.link1.get_html()
            mocked_get.assert_called_with()
            self.assertEqual(result.text, 'Success')

            mocked_get.return_value.ok = False
            mocked_get.return_value.text = 'Bad Response!'
            result = self.link2.get_html()
            mocked_get.assert_called_with()
            self.assertEqual(result.text, 'Bad Response!')

    def test_get_html_tags(self):
        self.assertListEqual(self.link1.get_html_tags(), TagSearcher('https://www.google.com').get_html_tags())
        self.assertListEqual(self.link2.get_html_tags(), TagSearcher('https://www.vk.com').get_html_tags())

    def test_count_tags(self):
        self.assertDictEqual(self.link1.count_tags(), TagSearcher('https://www.google.com').count_tags())
        self.assertDictEqual(self.link2.count_tags(), TagSearcher('https://www.vk.com').count_tags())


if __name__ == "__main__":
    unittest.main()
