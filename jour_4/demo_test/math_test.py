from unittest import TestCase, main
from _math import mult

class MathTest(TestCase):

    def test_mult(self):
        #AAA
        # Arrange
        x = 4
        y = 6
        expected = 24
        # Act
        result = mult(x,y)
        # Assert 
        self.assertEqual(result,expected)      

if __name__ == "__main__":
    main() # lancer le test