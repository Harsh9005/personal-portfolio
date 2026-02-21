---
title: "Why IVIVC Matters for Long-Acting Injectables"
date: "2026-02-01"
tags: ["IVIVC", "long-acting injectables", "regulatory"]
summary: "In vitro–in vivo correlations are essential for bridging dissolution testing with clinical outcomes — especially for complex depot formulations."
---

## The Regulatory Gap

Long-acting injectables (LAIs) present a unique regulatory challenge. Unlike oral dosage forms, where compendial dissolution testing is well-established, depot formulations require biorelevant release testing methods that capture the complex interplay between formulation properties and in vivo performance.

The FDA and EMA both recognize IVIVC as a pathway to reduce regulatory burden — enabling biowaivers for post-approval changes, setting clinically meaningful dissolution specifications, and supporting formulation bridging. Yet for injectable depots, the path to a validated IVIVC model remains significantly more challenging than for oral products.

## Why Standard Dissolution Falls Short

Traditional USP dissolution apparatus were designed for oral solid dosage forms. When applied to PLGA microspheres or in-situ forming implants, they fail to account for:

- **Tissue-level biomechanics** — shear stress, osmotic pressure, and enzymatic degradation at the injection site
- **Burst release dynamics** — the initial rapid release phase that determines early plasma exposure
- **Polymer degradation kinetics** — bulk vs. surface erosion mechanisms that govern long-term release

The result is a fundamental disconnect: the dissolution profile measured in a beaker may bear little resemblance to the drug release actually occurring at the subcutaneous or intramuscular injection site.

## Building the Bridge

IVIVC provides the mathematical framework to connect what we measure in the lab to what happens in the patient. For LAIs, this means developing release methods that are not just discriminating, but truly predictive of in vivo performance.

The three IVIVC levels offer different entry points:

- **Level A** — a point-to-point correlation between dissolution and absorption, the gold standard but demanding in data requirements
- **Level B** — a statistical moment comparison (mean dissolution time vs. mean residence time), simpler but less informative
- **Level C** — a single-point correlation between one dissolution parameter and one PK parameter, often the pragmatic first step

The key insight is that IVIVC is not just a regulatory checkbox — it is a scientific tool that forces us to understand our formulation at a mechanistic level. When a Level A correlation succeeds, it validates our entire in vitro testing strategy. When it fails, it tells us exactly where our understanding breaks down.

## What I Built

To make IVIVC methodology more accessible to formulation scientists, I developed an [interactive IVIVC Level Selection Dashboard](https://ivivc-level-selector.streamlit.app) that guides users through level selection and demonstrates each methodology with synthetic data. The goal is to lower the barrier to entry for scientists who know they need IVIVC but are unsure where to start.
