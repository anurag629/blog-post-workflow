from github import Github
import os
import dotenv

dotenv.load_dotenv()


def updateReadme(username, repository, table):
    token = os.getenv("GITHUB_ACCESS_TOKEN")
    g = Github(token)

    repo = g.get_repo(f"{username}/{repository}")
    readme = repo.get_readme()

    readme_content = readme.decoded_content.decode("utf-8")

    # Find the starting and ending delimiters in the README content
    start_delimiter = "<!--START_SECTION:latest_blog_posts-->"
    end_delimiter = "<!--END_SECTION:latest_blog_posts-->"

    # Check if the table already exists in the README content
    if start_delimiter in readme_content and end_delimiter in readme_content:
        # Update the section between the delimiters with the new table
        updated_content = readme_content.replace(
            readme_content[readme_content.find(start_delimiter) + len(start_delimiter):readme_content.find(end_delimiter)].strip(),
            table.strip()
        )
    else:
        # If the table does not exist, append the table to the end of the README content
        updated_content = readme_content + f"\n\n{start_delimiter}\n\n{table}\n\n{end_delimiter}"

    # Commit the updated content to the README file
    repo.update_file(
        path=readme.path,
        # add sucess emoji at the end of the commit message
        message="Update latest blog posts table :tada:",
        content=updated_content.encode("utf-8"),
        sha=readme.sha
    )