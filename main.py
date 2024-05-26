import frontmatter
import os
from bs4 import BeautifulSoup

def generate_table_rows(papers_directory):
    rows = []
    for filename in os.listdir(papers_directory):
        if filename.endswith(".md") and not filename.startswith("_"):
            filepath = os.path.join(papers_directory, filename)
            with open(filepath, 'r') as f:
                post = frontmatter.load(f)
                title = post.metadata.get('title', 'No Title')
                year = post.metadata.get('year', '')
                labels = post.metadata.get('labels', '')
                row_html = f'<tr data-labels="{labels}"><td><a href="https://github.com/angelicagardner/paper-collection/blob/main/talks/{filename}">{title}</a></td><td>{labels}</td><td>{year}</td></tr>'
                rows.append(row_html)
    return rows

def update_html_with_table_rows(html_file_path, rows):
    with open(html_file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
    tbody = soup.find('tbody')
    tbody.clear()
    for row_html in rows:
        new_row = BeautifulSoup(row_html, 'html.parser').tr
        tbody.append(new_row)
    with open(html_file_path, 'w', encoding='utf-8') as file:
        file.write(str(soup))

if __name__ == "__main__":
    papers_directory = './papers'
    html_file_path = 'index.html'
    rows = generate_table_rows(papers_directory)
    update_html_with_table_rows(html_file_path, rows)
