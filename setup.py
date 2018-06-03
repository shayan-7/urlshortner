
import re
from os.path import join, dirname
from setuptools import setup, find_packages


# reading package version (same way the sqlalchemy does)
with open(join(dirname(__file__), 'urlShortener', '__init__.py')) as v_file:
    package_version = re.compile(r".*__version__ = '(.*?)'", re.S).match(v_file.read()).group(1)


dependencies = [
    'restfulpy >= 0.41.3',
    'ujson',
    'aiohttp',
    'pymongo',
    'mako',
    'nanohttp',
    'bddrest',

    # Deployment
    'gunicorn',

    # testing
    'requests',
    'webtest',
    'nose'
]


setup(
    name="urlShortener",
    version=package_version,
    author="Shayan",
    author_email="shayn.rokrok@gmail.com",
    install_requires=dependencies,
    packages=find_packages(),
    test_suite="urlShortener.tests",
    entry_points={
        'console_scripts': [
            'urlShortener = urlShortener:urlShortener.cli_main'
        ]
    },
    message_extractors={'urlShortener': [
        ('**.py', 'python', None),
    ]},
)
