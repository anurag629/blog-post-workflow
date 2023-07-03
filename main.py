import os

from PIL import Image, ImageDraw, ImageFont

from utils.generateTable import generate_table
from utils.updateReadme import update_readme
from utils.fetchBlogPost import fetch_blog_posts







if __name__ == '__main__':
    rss_feed_url = 'https://www.codercops.tech/rss.xml'  # Replace with your actual RSS feed URL
    latest_posts = fetch_blog_posts(rss_feed_url, num_posts=5)

    table = generate_table(latest_posts)

    github_username = 'anurag629'
    repo_name = 'anurag629'
    update_readme(github_username, repo_name, table)
