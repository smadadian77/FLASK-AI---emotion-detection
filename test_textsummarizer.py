import unittest
import json
from sentiment_analysis import text_summarizer

class TestTextSummarizer(unittest.TestCase):
    def test_text_summarizer(self):
        text = "In the heart of a bustling city, amidst towering skyscrapers and bustling streets, lies a hidden oasis of tranquility. Here, time slows down, and the gentle rustling of leaves in the breeze replaces the constant hum of traffic. A quaint little café nestled in a quiet corner serves aromatic coffee and freshly baked pastries, where locals and tourists alike gather to savor moments of respite from the chaos outside"
        result = text_summarizer(text)
        data = json.loads(result)
        # Access the result value
        result = data['alephalpha']['result']
        expected_result = "This is a description of a café in the middle of a bustling city."
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
