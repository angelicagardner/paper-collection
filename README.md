# Paper Collection in Computer Science

This repository is dedicated to summarizing and organizing research papers across the field of computer science with focus on what is currently relevant for my work and interest.

The goal is to create a personal, structured knowledge base where each entry includes:

- A summary of the paper’s main contributions
- Publication metadata (authors, year, venue, publisher)
- Key insights and discussion points

> 🧭 This setup is inspired by [How to Organize your Data Science Articles with GitHub](https://towardsdatascience.com/how-to-organize-your-data-science-articles-with-github-b5b9427dad37) but adapted for academic research tracking.

## Repository Setup

### Viewing the Summaries

All paper summaries are located in the `/papers` directory and displayed on a GitHub Pages site as a searchable table.
Each summary file follows the structure of `papers/_example.md`.

### Adding a New Paper

1. **Open Issues**: Interesting papers yet to be read appear as open issues following a template.
2. **After Reading**: Summarize the paper in a new Markdown file in the /papers directory (on the dev branch).
3. **Open a Pull Request**: Reference the issue using #issue_number. A GitHub Action syncs the issue labels (publisher, year, research type, etc.) to the PR.
4. **GitHub Actions**: When merged, a workflow regenerates the website index automatically.

## Label System

The repository uses labels to categorize papers consistently:

### 1. Research Type 🟦

Indicates what kind of scientific contribution the paper makes.

| Type	| Description |	Example Keywords |
| --- | --- | --- | 
| Theoretical	| Develops models, frameworks, or formal proofs without direct experimentation.	| Algorithms, models, formal methods |
| Empirical / Case Study | Based on observation, measurement, experimentation, or data collection. | Case study, benchmark, survey, measurement |
| Design / Tool	| Proposes a new system, method, or tool and demonstrates or evaluates it. | Architecture, prototype, implementation |
| Conceptual / Position |	Introduces new ideas or perspectives; may argue a viewpoint without empirical data.	| Vision paper, manifesto |
| Survey / Review	| Synthesizes and compares existing research on a topic. | Literature review, mapping study |

### 2. Item Type 🟩

Describes how and where the paper was published.

| Type | Description | 
| --- | --- |
| Journal Article | Peer-reviewed research published in a scientific journal. |
| Conference Paper | Peer-reviewed research presented at a scientific conference. |
| Workshop Paper | Preliminary or specialized research, usually shorter than a conference paper. |
| Preprint / Technical Report	| Research not yet peer-reviewed, often shared on arXiv or ResearchGate. |
| White Paper / Industry Report |	Practitioner-oriented document outlining applied research or a technology proposal. |
| Thesis / Dissertation	| Academic research submitted for a degree. |

### 3. Publisher 🟪 and Year 🟨

Used for filtering or sorting papers by publication context e.g., ACM, IEEE, Springer, arXiv.

### 4. Domain & Topic Labels 🟥

These describe the content of the paper e.g., observability, monitoring, cloud native, scalability, telecom.

## Disclaimer

This repository is licensed under the [MIT License](LICENSE). All original conference talks, videos and links referenced in this repository are the intellectual property of their respective authors, speakers, and organizations. The summaries and "Key Takeaways" provided are my personal study notes and interpretations. They are intended for educational and research purposes under "Fair Use" principles. This repository does not host or redistribute original copyrighted files (video files).
