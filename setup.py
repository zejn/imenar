#!/usr/bin/python


from distutils.core import setup

setup(name='imenar',
    version='1.0',
    description='Imenar - split slovenian name_surname into (name, surname)',
    author='Gasper Zejn',
    author_email='zejn@kiberpipa.org',
    url='http://github.com/zejn/imenar/',
    packages=['imenar'],
    package_data={'imenar': ['imena.csv', 'priimki.csv', 'test.csv']},
)
