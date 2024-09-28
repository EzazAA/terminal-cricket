from setuptools import setup, find_packages

setup(
    name='cricket',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'colorama',  # List any additional dependencies here
    ],
   entry_points={
    'console_scripts': [
        'cricket=game_files.main:play_game',  # Command to run the game
    ],
},

    description='A simple terminal game depicting cricket',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Ezaz Alam Ahmed ',
    author_email='ezazalamahmed@gmail.com',
    url='https://github.com/ezazaa/terminal-cricket',  # Update with your repository URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
