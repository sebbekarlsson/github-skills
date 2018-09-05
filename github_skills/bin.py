import sys
from tabulate import tabulate
from github_skills import get_skills


def run():
    if len(sys.argv) < 2:
        print('Usage: github-skills <username>')
        return

    skills = get_skills(sys.argv[1])

    print(tabulate(
        [(s['language'], '{}%'.format(s['percentage'])) for s in skills],
        headers=['language', 'percentage']
    ))
