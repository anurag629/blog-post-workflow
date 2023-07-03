from github import Github

def saveImage()
    

    g=Github("Git Token")
    repo=g.get_repo("Repo")

    file_path = "Image.png"
    message = "Commit Message"
    branch = "master"

    with open(file_path, "rb") as image:
        f = image.read()
        image_data = bytearray(f)

    def push_image(path,commit_message,content,branch,update=False):
        if update:
            contents = repo.get_contents(path, ref=branch)
            repo.update_file(contents.path, commit_message, content, sha=contents.sha, branch)
        else:
            repo.create_file(path, commit_message, content, branch)


push_image(file_path,message, bytes(image_data), branch, update=False)