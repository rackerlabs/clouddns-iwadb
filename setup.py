from setuptools import setup, find_packages


setup(
    name='iwadb',
    packages=find_packages(),
    install_requires=['click'],
    entry_points={
        'console_scripts': [
            'iwadb = iwadb.cli:main',
        ]
    }
)
