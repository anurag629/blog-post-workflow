import feedparser
import os
from utils.generateImage import generateImage

def fetchBlogPost(feed_url, num_posts=5, font_type ='NightPumpkind'):
    feed = feedparser.parse(feed_url)
    posts = []
    for entry in feed.entries[:num_posts]:
        title = entry.title
        description = entry.description
        link = entry.link
        image_url = entry.image.url if 'image' in entry else None

        if image_url is None:
            if font_type == 'NightPumpkind':
                image_url = generateImage(title, r'fonts\night-pumpkind-font\NightPumpkind-1GpGv.ttf')
            elif font_type == 'NestroCopper':
                image_url = generateImage(title, r'fonts\nesto-copper-42-font\Nestocopper42-1GVw2.ttf')
            else:
                image_url = generateImage(title, r'fonts\coffee-healing-font\CoffeeHealing-1GrKe.ttf')


        post = {
            'title': title,
            'description': description,
            'link': link,
            'image_url': image_url
        }
        posts.append(post)
    return posts