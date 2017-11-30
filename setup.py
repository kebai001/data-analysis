from setuptools import setup, find_packages

setup(
    name='data_analysis',
    version='0.0.1',
    url='www.github.com/kebai001/data-analysis',
    license='BSD',
    author='Ke Bai',
    packages=find_packages(),
    install_requires=['PyQt5',
                      'pandas',
                      'sqlalchemy',
                      'nltk',
                      'numpy',
                      'jupyter',
                      'python-twitter',
                      'tweepy'],
    entry_points={},
    extra_require={'dev': ['flake8',]}
)