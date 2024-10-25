import requests

def create_issue(owner, repo, title, body, assignees=[], labels=[]):
  """Creates an issue on GitHub using the API.

  Args:
      owner: The owner of the repository.
      repo: The name of the repository.
      title: The title of the issue.
      body: The body of the issue.
      assignees: A list of usernames to assign the issue to. (optional)
      labels: A list of label names for the issue. (optional)

  Returns:
      A dictionary containing the response data from the GitHub API.
  """

  url = f"https://api.github.com/repos/{owner}/{repo}/issues"

  headers = {
      "Accept": "application/vnd.github+json",
      "Authorization": f"Bearer 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",
      "X-GitHub-Api-Version": "2022-11-28"  # Replace with the latest version if needed
  }

  data = {
      "title": title,
      "body": body,
      "assignees": ["purpleraiin"],
      "labels": ["bug"],
      "milestone": None  # Set milestone to null for "no milestone"
  }

  response = requests.post(url, json=data, headers=headers)

  if response.status_code == 201:
      print("Issue created successfully!")
      return response.json()  # Return the response data for further processing
  else:
      print("Error creating issue:", response.text)
      return None

# Replace with your information
owner = "purpleraiin"
repo = "Test-Project"
title = "Sample Issue 3 with label 23 october"
body = "This is a sample issue 2 with label created using the GitHub API."
labels = ["bug","country"]

response_data = create_issue(owner, repo, title, body, labels)

# You can access the response data if successful (e.g., issue number)
if response_data:
  issue_number = response_data["number"]
  print(f"Issue created with number: {issue_number}")