from github import Github
import os
import re
import dotenv

dotenv.load_dotenv()

def saveNewImages(username, repository, posts):
    token = os.getenv("GITHUB_ACCESS_TOKEN")
    g = Github(token)
    
    repo = g.get_repo(f"{username}/{repository}")
    images_dir = "images"
    os.makedirs(images_dir, exist_ok=True)
    for post in posts:
        title = post['title']
        image_url = post['image_url']
        
        title = re.sub(r'[^a-zA-Z\s]', '_', title)
        title = title.replace(' ', '_')
        image_path = os.path.join(images_dir, f"{title}.jpg")
        repo.create_file(image_path, "Add new image", open(image_path, 'rb').read())
        post['image_url'] = f"https://github.com/{username}/{repository}/raw/main/{image_path}"
    return posts
