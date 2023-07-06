from utils.fetchBlogPost import fetchBlogPost
from utils.generateTable import generateTable
from utils.updateReadme import updateReadme






if __name__ == '__main__':
    rss_feed_url = 'https://www.codercops.tech/rss.xml'  # Replace with your actual RSS feed URL
    latest_posts = fetchBlogPost(rss_feed_url, num_posts=5)

    table = generateTable(latest_posts)

    github_username = 'anurag629'
    repo_name = 'anurag629'
    updateReadme(github_username, repo_name, table)
