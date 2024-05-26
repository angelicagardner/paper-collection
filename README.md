# Paper Collection in Computer Science

This repo setup was inspired by (but doesn't exactly follow): [How to Organize your Data Science Articles with Github](https://towardsdatascience.com/how-to-organize-your-data-science-articles-with-github-b5b9427dad37)

## About

This repository is dedicated to summarizing research papers in the field of computer science. Each entry includes a summary, publication details, key insights, and potential discussion points about the research presented. The goal for this repository is to serve as a resource (for myself) to store and quickly access the essence of these papers.

## Repository Setup

### Viewing the Summaries

The papers are displayed on a GitHub Pages site that contains a table linking to individual Markdown files for each paper. These files are located in the `/papers` directory.

### Adding a New Paper

1. **Open Issues**: If there's an interesting paper not yet summarized, it will appear as an open Issue. The issues follow an Issue Template.
2. **After Reading**: The paper will be summarized in a new Markdown file in the `/papers` directory under the "dev" branch. The Markdown file should follow the setup in `papers/_example.md`.
3. **Open a Pull Request**: Once the summary is ready, a pull request can be created and merged to the main branch. It's important to mention the associated issue using `#issue_number` format in the pull request - this will trigger a workflow that adds the same issue labels to the PR.
4. **GitHub Actions**: The merged changes will trigger a Workflow that updates the webpage so the new paper is added to the table.

---

Welcome to Paper Collection in Computer Science: Unveiling Knowledge from the Realm of Research!

### Prerequisities 

For the setup to work, the repository needs to have a **Actions secret** created in **Settings**. The secret will be a pasted personal access token (PAT) generated from GitHub Profile **Developer settings**. 
