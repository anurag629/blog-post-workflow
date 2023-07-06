import feedparser
import os
from utils.generateImage import generateImage

def fetchBlogPost(feed_url, num_posts=5):
    feed = feedparser.parse(feed_url)
    posts = []
    for entry in feed.entries[:num_posts]:
        title = entry.title
        description = entry.description
        link = entry.link
        image_url = entry.image.url if 'image' in entry else None

        if image_url is None:
            image_url = generateImage(title, '/content/NightPumpkind-1GpGv.ttf')  # Generate image and get the image URL

        post = {
            'title': title,
            'description': description,
            'link': link,
            'image_url': image_url
        }
        posts.append(post)
    return posts