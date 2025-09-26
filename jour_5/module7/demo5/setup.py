from setuptools import setup
from Cython.Build import cythonize

setup(
    name="mymath_cy",
    ext_modules=cythonize("mymath_cy.pyx", language_level = 3)
)