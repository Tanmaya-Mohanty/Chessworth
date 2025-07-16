from setuptools import setup, find_packages

setup(
    name='chessworth',
    version='0.1',
    description='Chessworth variant: low-value captures of high-value produce mutual destruction',
    author='Tanmaya Mohanty',
    url='https://github.com/Tanmaya-Mohanty/chessworth',
    packages=find_packages(),
    install_requires=[
        'python-chess',
        'IPython'
    ],
    entry_points={
        'console_scripts': [
            'chessworth=chessworth:play_game'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Topic :: Games/Entertainment :: Board Games',
        'License :: OSI Approved :: MIT License',
    ],
)
