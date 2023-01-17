import unittest
from translator import french_to_english, english_to_french


class TestEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hello")['translations'][0]['translation'], "Bonjour")


class TestFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("Bonjour")['translations'][0]['translation'], "Hello")


if __name__ == '__main__':
    unittest.main()
