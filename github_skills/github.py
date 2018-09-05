import requests
import json


def get_skills(username):
    skills = {}
    resp = requests.get('https://api.github.com/users/' + username + '/repos')
    repos = json.loads(resp.text)
    count = 0

    for repo in filter(lambda x: x['language'] is not None, repos):
        skills[repo['language']] = 1 if repo['language'] not in skills else\
            skills[repo['language']] + 1

        count += 1

    return map(
        lambda x: {
            'language': x[0],
            'percentage': (float(x[1]) / float(count)) * 100
        },
        skills.items()
    )
