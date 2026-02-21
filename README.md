# Personal Portfolio — Harshvardhan Modh, Ph.D.

[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B.svg)](https://streamlit.io)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-green.svg)](https://python.org)

> Personal portfolio and blog for Harshvardhan Modh, Ph.D. — pharmaceutical
> scientist specializing in nanomedicine, IVIVC, and computational modeling.

## Structure

```
personal-portfolio/
├── 0_🏠_About_Me.py          # About Me (landing page)
├── pages/
│   ├── 1_🔬_Projects.py     # Tools & scientific software
│   ├── 2_📚_Publications.py # Selected publications
│   └── 3_📝_Blog.py         # Markdown-based blog
├── blog/                     # Blog posts (add .md files here)
├── .streamlit/config.toml    # Material Blue theme
├── requirements.txt
└── README.md
```

## Adding a Blog Post

Create a new `.md` file in the `blog/` directory with YAML frontmatter:

```markdown
---
title: "Post Title"
date: "2026-03-01"
tags: ["tag1", "tag2"]
summary: "Brief description"
---

Your post content in Markdown...
```

Push to GitHub and the blog updates automatically via Streamlit Community Cloud.

## Local Development

```bash
git clone https://github.com/Harsh9005/personal-portfolio.git
cd personal-portfolio
pip install -r requirements.txt
streamlit run "0_🏠_About_Me.py"
```

## License

MIT
