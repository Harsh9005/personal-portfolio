---
title: "Building Computational Tools for Pharmaceutical Scientists"
date: "2026-01-15"
tags: ["Python", "Streamlit", "open source", "pharmaceutical development"]
summary: "Why I build open-source tools for pharmaceutical R&D, and why Streamlit is the ideal framework for scientific dashboards."
---

## The Problem

Pharmaceutical development generates enormous amounts of data — dissolution profiles, pharmacokinetic curves, microscopy images, stress-strain measurements. Yet most scientists still analyze this data using Excel spreadsheets and manual workflows.

The bottleneck is not computational power. It is **accessibility**. Most scientific computing tools require programming expertise that bench scientists do not have, and most web applications require deployment infrastructure that academic labs cannot maintain.

This creates a gap: the scientist who understands the problem cannot build the tool, and the developer who can build the tool does not understand the problem.

## Why Streamlit

Streamlit closes this gap. It is the first framework I have found that genuinely allows a scientist to build and deploy a professional web application without leaving Python:

1. **Pure Python** — no HTML, CSS, or JavaScript required
2. **Interactive widgets** — sliders, dropdowns, and file uploaders map naturally to scientific parameters
3. **Free deployment** — Streamlit Community Cloud provides zero-cost hosting with GitHub integration
4. **Shareable** — a URL replaces "please install Python and run this script"

For a pharmaceutical scientist, this means the IVIVC model you built in a Jupyter notebook can become a live web tool that your collaborators (and regulators) can interact with — in an afternoon.

## What I Have Built

I have focused on tools that address specific, recurring bottlenecks in pharmaceutical R&D:

- **[IVIVC Level Selector](https://ivivc-level-selector.streamlit.app)** — a decision-support tool that guides scientists through FDA/EMA IVIVC methodology selection, with interactive tutorials for each level
- **[SEM Pore Analyzer](https://github.com/Harsh9005/sem-pore-analysis)** — automated pore size quantification from microscopy images, replacing manual caliper measurements
- **[Crystal Area Analyzer](https://github.com/Harsh9005/polarized-microscopy-crystal-analysis)** — polymorphism screening from polarized light microscopy, designed for crystallization process monitoring
- **[Wall Shear Stress Visualizer](https://github.com/Harsh9005/shear-stress-3d-viz)** — 3D hemodynamic flow visualization supporting our nanomedicine research

Each tool is designed to replace a manual, error-prone workflow with a reproducible, documented alternative.

## The Principle

Every tool I build follows the same principle: **if I had to do this analysis more than twice, it deserves a tool. And if the tool could help someone else, it deserves to be open source.**

The pharmaceutical industry has a long tradition of sharing methods through publications. Open-source scientific software is the natural extension of that tradition — sharing not just the method, but the implementation.
