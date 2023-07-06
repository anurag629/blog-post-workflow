def generateTable(posts):
    table = '<!--START_SECTION:latest_blog_posts-->\n'
    table += "| Title | Description | Image |\n"
    table += "| --- | --- | --- |\n"
    for post in posts:
        title = post['title']
        description = post['description']
        image_url = post['image_url']
        link = post['link']
        table += f"| [{title}]({link}) | {description} | ![Image]({image_url}) |\n"
    # table += "<!--END_SECTION:latest_blog_posts-->\n"
    return table