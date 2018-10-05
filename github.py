from github import Github
from config import github_token
import requests

g = Github(github_token)
url = 'https://api.github.com/graphql'
json = { 'query' : '{ viewer { repositories(first: 30) { totalCount pageInfo { hasNextPage endCursor } edges { node { name } } } } }' }
api_token = "your api token here..."
headers = {'Authorization': 'token %s' % github_token}

r = requests.post(url=url, json=json, headers=headers)
print (r.text)

# for repo in g.get_user().get_repos():
#     print(repo.name)

# fetch repos of user

# fetch users of repo

# fetch user info of repo



# fetch general user info

# fetch general repo info