import feedparser
import os
from utils.generateImage import generate_image

def fetch_blog_posts(feed_url, num_posts=5):
    feed = feedparser.parse(feed_url)
    posts = []
    images_dir = "images"
    os.makedirs(images_dir, exist_ok=True)
    
    # Delete previous images in the folder
    for file_name in os.listdir(images_dir):
        file_path = os.path.join(images_dir, file_name)
        os.remove(file_path)
    
    for entry in feed.entries[:num_posts]:
        title = entry.title
        description = entry.description
        link = entry.link
        image_url = entry.image.url if 'image' in entry else None

        if image_url is None:
            image = generate_image(title)
            image_path = os.path.join(images_dir, f"{title.replace(' ', '_')}.jpg")
            image.save(image_path)
            image_url = f"https://github.com/anurag629/anurag629/raw/main/{image_path}"

        post = {
            'title': title,
            'description': description,
            'image': image_url,
            'link': link
        }
        posts.append(post)
    
    return posts