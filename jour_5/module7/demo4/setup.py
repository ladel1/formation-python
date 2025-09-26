from setuptools import setup, Extension

setup(
    name = "mymodule",
    version = "1.0.0",
    description = "demo c extension",
    ext_modules = [Extension("mymodule",["mymodule.c"])]
)