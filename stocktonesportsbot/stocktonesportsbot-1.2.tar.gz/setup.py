from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(name='stocktonesportsbot',
    version='1.2',
    description='''A Discord bot for Stockton University's Esports Discord Server''',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Dual-Exhaust/Stockton-Esports-Bot',
    author='Dual-Exhaust',
    author_email='kylecsacco@gmail.com',
    license='MIT',
    packages=['stocktonesportsbot', 'stocktonesportsbot/classes'],
    scripts=['bin/startbot', 'bin/launch.sh'],
    python_requires='>=3.7',
    install_requires=['aiohttp==3.5.4',
        'async-timeout==3.0.1',
        'attrs==19.1.0',
        'beautifulsoup4==4.8.0',
        'certifi==2019.6.16',
        'chardet==3.0.4',
        'cycler==0.10.0',
        'discord.py==1.2.3',
        'idna==2.8',
        'kiwisolver==1.1.0',
        'matplotlib==3.1.1',
        'multidict==4.5.2',
        'numpy==1.17.1',
        'oauthlib==3.1.0',
        'pandas==0.25.1',
        'pyparsing==2.4.2',
        'PySocks==1.7.0',
        'python-dateutil==2.8.0',
        'pytz==2019.2',
        'requests==2.22.0',
        'requests-oauthlib==1.2.0',
        'six==1.12.0',
        'soupsieve==1.9.3',
        'tweepy==3.8.0',
        'urllib3==1.25.3',
        'websockets==6.0',
        'yarl==1.3.0'],
    include_package_data=True,
    zip_safe=False)
