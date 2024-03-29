from setuptools import find_packages, setup

REQUIRES = [
    'Django==5.0.3',
    'psycopg2-binary==2.9.9',
    'setuptools==69.1.1',
    'pip==24.0',
    'djangorestframework==3.15.1',
    "geopy==2.4.1",
    "django-filter==24.2"
]

CODESTYLE_REQUIRES = [
    'flake8==7.0.0',
    'isort==5.13.2',
]

setup(
    name='search_for_cars',
    packages=find_packages(),
    install_requires=REQUIRES,
    extras_require={'codestyle': CODESTYLE_REQUIRES}
)
