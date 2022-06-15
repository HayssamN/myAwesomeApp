import unittest
from app import mystr

class TestStringMethods(unittest.TestCase):

   
    def test_upper(self):
        t1=mystr('my fRiend')
        self.assertEqual(t1.toUpperCase(), 'MY FRIEND')

    def test_lower(self):
        t1=mystr('mY fRiend')
        self.assertEqual(t1.toLowerCase(), 'my friend')
