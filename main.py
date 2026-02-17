import frontmatter
import markdown2
import os
from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader

def generate_table_rows(papers_dir):
    rows = []
    for filename in os.listdir(papers_dir):
        if filename.endswith(".md") and not filename.startswith("_"):
            filepath = os.path.join(papers_dir, filename)
            with open(filepath, 'r') as f:
                post = frontmatter.load(f)
                title = post.metadata.get('title', 'No Title')
                year = post.metadata.get('year', '')
                labels = post.metadata.get('labels', '')
                row_html = f'<tr data-labels="{labels}"><td><a href="https://github.com/angelicagardner/paper-collection/blob/main/papers/{filename}">{title}</a></td><td>{labels}</td><td>{year}</td></tr>'
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

def generate_paper_pages(papers_dir, template_path, output_dir):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(template_path)

    for filename in os.listdir(papers_dir):
        if filename.endswith(".md") and not filename.startswith("_"):
            filepath = os.path.join(papers_dir, filename)
            with open(filepath, 'r') as f:
                post = frontmatter.load(f)
                title = post.metadata.get('title', 'No Title')
                year = post.metadata.get('year', '')
                labels = post.metadata.get('labels', '').split(', ')
                summary = post.content.split('\n')[0]
                markdown_content = post.content
                html_content = markdown2.markdown(markdown_content)

                rendered_html = template.render(
                    title=title,
                    year=year,
                    labels=labels,
                    summary=summary,
                    content=html_content,
                )

                output_filename = filename.replace('.md', '.html')
                output_path = os.path.join(output_dir, output_filename)
                os.makedirs(output_dir, exist_ok=True)
                with open(output_path, 'w', encoding='utf-8') as out_file:
                    out_file.write(rendered_html)

if __name__ == "__main__":
    papers_dir = './papers'
    html_file_path = 'index.html'
    template_path = 'template.html'
    papers_output_dir = papers_dir + '/html'
    
    rows = generate_table_rows(papers_dir)
    update_html_with_table_rows(html_file_path, rows)

    generate_paper_pages(papers_dir, template_path, papers_output_dir)
