from config import github_token
import requests, json

_url = 'https://api.github.com/graphql'
_json = { 'query' : '{ viewer { repositories(first: 30) { totalCount pageInfo { hasNextPage endCursor } edges { node { name } } } } }' }
_headers = {'Authorization': 'token %s' % github_token}

r = requests.post(url=_url, json=_json, headers=_headers)
json_res = json.loads(r.text)

print(json.dumps(json_res, indent=2))

# for repo in g.get_user().get_repos():
#     print(repo.name)

# fetch repos of user

# fetch users of repo

# fetch user info of repo



# fetch general user info

# fetch general repo info