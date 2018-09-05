from setuptools import setup, find_packages


setup(
    name='github-skills',
    version='1.0',
    install_requires=[
        'requests',
        'tabulate'
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'github-skills = github_skills.bin:run'
        ]
    }
)
