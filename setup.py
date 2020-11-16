from setuptools import setup
import os

with open(os.path.join(os.path.dirname(__file__), "LYRICS_STATISTICS", "version.py")) as r:
    exec(r.read())
setup(
    name=__id__,
    version=__version__,
    description='Lyrics Statistics',
    author='Sirisha Bajanki',
    author_email='bssiri@gmail.com',
    packages=['LYRICS_STATISTICS'],
    scripts=['bin/lyrics_statistics.py'],
    install_requires=['fire','numpy', 'requests'],
    python_requires='~=3.6',
)
