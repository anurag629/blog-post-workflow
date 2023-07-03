from github import Github

def update_readme(username, repository, table):
    token = "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"  # Replace with your personal access token
    g = Github(token)
    
    repo = g.get_repo(f"{username}/{repository}")
    readme = repo.get_readme()
    
    readme_content = readme.decoded_content.decode("utf-8")
    
    # Find the starting and ending delimiters in the README content
    start_delimiter = "<!--START_SECTION:latest_blog_posts-->"
    end_delimiter = "<!--END_SECTION:latest_blog_posts-->"
    
    # Update the section between the delimiters with the new table
    updated_content = readme_content.replace(
        readme_content[readme_content.find(start_delimiter) + len(start_delimiter):readme_content.find(end_delimiter)].strip(),
        table.strip()
    )
    
    # Commit the updated content to the README file
    repo.update_file(
        path=readme.path,
        message="Update latest blog posts",
        content=updated_content.encode("utf-8"),
        sha=readme.sha
    )