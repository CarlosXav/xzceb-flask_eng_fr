import unittest
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

import translator

class TestTranslator(unittest.TestCase):
    def test_english_to_french(self):
        self.assertNotEqual(translator.english_to_french('Banana'), 'Invalid input.')
        self.assertEqual(translator.english_to_french('Goodbye'), 'Au revoir')
        self.assertEqual(translator.english_to_french('Hello'), 'Bonjour')
        self.assertEqual(translator.english_to_french(None), 'Invalid input.')
    
    def test_french_to_english(self):
        self.assertNotEqual(translator.french_to_english('Banana'), "Entrée invalide.")
        self.assertEqual(translator.french_to_english('Au revoir'), 'Goodbye')
        self.assertEqual(translator.french_to_english('Bonjour'), 'Hello')
        self.assertEqual(translator.french_to_english(None), "Entrée invalide.")

if __name__=='__main__':
    unittest.main()
