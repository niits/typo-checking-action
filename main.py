

import argparse
from github import Github
import requests
from pprint import pprint
import base64
import json


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('--sha', action='store', required=True, type=str)
    parser.add_argument('--token', action='store',required=True, type=str)
    parser.add_argument('--repo_name', action='store', type=str)

    args = parser.parse_args()

    sha = vars(args)['sha']
    token = vars(args)['token']
    repo_name = vars(args)['repo_name']

    g = Github(token)
    repo = g.get_repo(repo_name)
    commit = repo.get_commit(sha=sha)

    for file in commit.files:
        respone = requests.get(file.contents_url, headers={
            'Authorization': 'token ' + token
        })

        data = json.loads(respone.text)
        content = base64.b64decode(data['content']).decode('utf-8')