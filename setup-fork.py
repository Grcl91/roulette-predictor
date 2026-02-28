import os
from github import Github

# Initialize using an access token
access_token = os.getenv('GITHUB_ACCESS_TOKEN')
g = Github(access_token)

# Example of getting a repository
repo = g.get_repo('owner/repo_name')

# Example: List the issues in the repository
issues = repo.get_issues()
for issue in issues:
    print(issue.title)