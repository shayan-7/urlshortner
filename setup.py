import re
from os.path import join, dirname
from setuptools import setup, find_packages


# reading package version (same way the sqlalchemy does)
with open(join(dirname(__file__), 'urlshortener', '__init__.py')) as v_file:
    package_version = re.compile('.*__version__ = \'(.*?)\'', re.S)\
        .match(v_file.read()).group(1)


dependencies = [
    'restfulpy >= 0.41.3',
    'hashids',
    'nanohttp',
    'oauth2client',
    'requests',
    'sqlalchemy',

    # Deployment
    'gunicorn',

    # testing
    'webtest',
    'nose',
    'bddrest'
]


setup(
    name='urlshortener',
    version=package_version,
    author='Mohammad',
    author_email='mohammadsheikhian70@gmail.com',
    install_requires=dependencies,
    packages=find_packages(),
    test_suite='urlshortener.tests',
    entry_points={
        'console_scripts': [
            'urlshortener = urlshortener:urlshortener.cli_main'
        ]
    }
)

