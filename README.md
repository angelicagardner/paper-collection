# List of scholarly articles and research papers in AI/ML

A repository for organizing AI/ML scholarly articles and research papers for the purpose of keeping a future reference to interesting ones I've read, quickly review the key points of the articles, and keep track of my reading. 

This repo setup is inspired by the following article: [How to Organize your Data Science Articles with Github](https://towardsdatascience.com/how-to-organize-your-data-science-articles-with-github-b5b9427dad37)


## Format

1. Articles and papers are created as Issues and information is filled in according to a template.
2. The name of the article/paper is used as the title of the Issue.
3. Each issue contains the following information:
    - TL;DR - A short summary (~140 characters). It should capture the essence of the problem being solved, the solution/approach the author(s) have taken and the results.
    - Author(s)
    - DOI - Unique alphanumeric string assigned to a digital document. It serves as a permanent link to the document. 
    - Related link - To an associated code repo or similar.
    - Key Takeaways - The parts I found useful.
    - Comments/Questions - My thoughts/opinions or questions on the paper and/or its results are provided in the comment setion of the Issue.
    - Labels are used to assign categories to the article/paper accordingly.


## Setup

In this repo, there is a GitHub Actions workflow set up to automate the process of generating an HTML file from the issues (articles/papers) and pushing the changes back to the repository to deploy on GitHub pages. The workflow is triggered manually and it utilizes a Python script and environment variables to achieve this. The Python script uses the GitHub API to fetch and manage the issues. It retrieves a list of issues (excluding pull requests) and generates the HTML file `index.html` to present the articles/papers in a structured format, including Title, Author and Lables.


### Prerequisities 

For the setup to work, the repository needs to have a **Actions secret** created in **Settings**. The secret will be a pasted personal access token (PAT) generated from GitHub Profile **Developer settings**. 