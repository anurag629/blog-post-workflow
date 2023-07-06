from github import Github
import dotenv
import os

dotenv.load_dotenv()

def deletePreviousImages(username, repository):
    token = os.getenv("GITHUB_ACCESS_TOKEN")
    g = Github(token)
    
    repo = g.get_repo(f"{username}/{repository}")
    contents = repo.get_contents("images")
    for content in contents:
        if content.type == "file":
            repo.delete_file(content.path, "Delete previous images", content.sha)
