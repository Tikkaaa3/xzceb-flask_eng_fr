import unittest
from translator import english_to_french, french_to_english


class test_translator(unittest.TestCase):
    
    def test_english_to_french(self):
        translated1 = english_to_french('Hello')
        self.assertEqual(translated1, 'Bonjour')
    
        translated2 = english_to_french('Hello')
        self.assertNotEqual(translated2 , 'Comment vas-tu')
    
    def test_french_to_english(self):
        translated = french_to_english('Bonjour')
        self.assertEqual(translated , 'Hello')

        translated2 = french_to_english('Comment vas-tu')
        self.assertNotEqual(translated2 , 'Hello')

    



if __name__ == '__main__':
    unittest.main()