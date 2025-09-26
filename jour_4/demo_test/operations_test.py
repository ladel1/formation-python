"""
Doc unittests https://docs.python.org/3/library/unittest.html
"""
from unittest import TestCase, main
from operations import caree, div, factorielle

class OperationsTest(TestCase):

    def test_caree(self):
        #AAA
        # Arrange
        x = 4
        expected = 16
        # Act
        result = caree(x)
        # Assert 
        self.assertEqual(result,expected)       

    def test_div(self):
        # pas trop de responsabilités => réponsabilité unique
        # AAA
        # Arrange
        a = 10
        q = 2
        expected = 5
        # Act
        result = div(a,q)
        # Assert
        self.assertEqual(result,expected)

    def test_division_sur_zero(self):
        # pas trop de responsabilités => réponsabilité unique
        # AAA
        # Arrange
        a = 10
        q = 0        
        # Assert
        with self.assertRaises(Exception):
            # Act
            result = div(a,q)

    def test_factorielle(self):
        """
        TDD
        """
        # AAA
        #Arrange
        n = 5
        expected = 120
        #act
        result = factorielle(n)
        #Assert
        self.assertEqual(result,expected)

if __name__ == "__main__":
    main() # lancer le test