def generate_table(posts):
    table = "| Title | Description | Image |\n"
    table += "| --- | --- | --- |\n"
    for post in posts:
        title = post['title']
        description = post['description']
        image = post['image']
        link = post['link']
        table += f"| [{title}]({link}) | {description} | ![Image]({image}) |\n"
    return table