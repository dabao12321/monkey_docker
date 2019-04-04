from setuptools import setup

setup(
    name='monkey',
    version='0.0.1',
    description='The Monkey CLI',
    url='https://github.com/dabao12321/monkey_docker.git',
    packages=[
        'monkey',
    ],
    entry_points={
        'console_scripts': [
            'monkey = monkey.__main__:main',
        ],
    },
)
