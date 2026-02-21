"""
Page 3: Blog — Markdown-based blog system

Reads .md files from the blog/ directory. Each file should have YAML
frontmatter:

---
title: "Post Title"
date: "2026-02-01"
tags: ["tag1", "tag2"]
summary: "Brief description"
---

Post content in Markdown ...
"""

import streamlit as st
import os
import yaml
from datetime import datetime

st.set_page_config(
    page_title="Blog — Harshvardhan Modh",
    page_icon="📝",
    layout="wide",
)

BLOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "blog")


def parse_blog_post(filepath: str) -> dict:
    """Parse a markdown file with YAML frontmatter.

    Returns a dict with keys:
        title, date, date_str, tags, summary, content, filename
    """
    with open(filepath, "r", encoding="utf-8") as fh:
        raw = fh.read()

    # Split on YAML frontmatter delimiters (--- ... ---)
    if raw.startswith("---"):
        parts = raw.split("---", 2)
        if len(parts) >= 3:
            frontmatter = yaml.safe_load(parts[1]) or {}
            content = parts[2].strip()
        else:
            frontmatter = {}
            content = raw
    else:
        frontmatter = {}
        content = raw

    # Parse date for sorting
    date_str = str(frontmatter.get("date", "2000-01-01"))
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        date_obj = datetime.min

    return {
        "title": frontmatter.get("title", os.path.basename(filepath)),
        "date": date_obj,
        "date_str": date_str,
        "tags": frontmatter.get("tags", []),
        "summary": frontmatter.get("summary", ""),
        "content": content,
        "filename": os.path.basename(filepath),
    }


def load_all_posts() -> list[dict]:
    """Load all .md files from the blog directory, sorted newest first."""
    if not os.path.isdir(BLOG_DIR):
        return []

    posts = []
    for fname in os.listdir(BLOG_DIR):
        if fname.endswith(".md"):
            posts.append(parse_blog_post(os.path.join(BLOG_DIR, fname)))

    posts.sort(key=lambda p: p["date"], reverse=True)
    return posts


# ── Page Content ────────────────────────────────────────────────────────────
st.title("📝 Blog")
st.markdown(
    "### Thoughts on pharmaceutical R&D, computational tools, and nanomedicine"
)

st.markdown("---")

posts = load_all_posts()

if not posts:
    st.info("No blog posts yet. Check back soon!")
else:
    for post in posts:
        with st.expander(
            f"**{post['title']}** — {post['date_str']}",
            expanded=False,
        ):
            # Tags
            if post["tags"]:
                tag_str = " ".join(f"`{tag}`" for tag in post["tags"])
                st.markdown(tag_str)

            # Summary
            if post["summary"]:
                st.markdown(f"*{post['summary']}*")
                st.markdown("")

            # Full content
            st.markdown(post["content"])

        st.markdown("")  # spacing between posts

st.markdown("---")
st.caption(
    "To add a new post: create a .md file in the blog/ directory with "
    "YAML frontmatter, then push to GitHub."
)
