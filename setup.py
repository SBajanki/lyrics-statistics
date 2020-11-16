from setuptools import setup
import os

with open(os.path.join(os.path.dirname(__file__), "LYRICS_STATISTICS", "1.0")) as r:
    exec(r.read())
setup(
    name= 'LYRICS_STAT',
    version= '1.0',
    description='Lyrics Statistics',
    author='Sirisha Bajanki',
    author_email='bssiri@gmail.com',
    packages=['LYRICS_STAT'],
    scripts=['bin/lyrics_statistics.py'],
    install_requires=['fire','numpy', 'requests'],
    python_requires='~=3.6',
)
