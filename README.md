# Career Discovery AI - Project

# Career Discovery AI

Career Discovery AI is a beginner-friendly **Machine Learning and Natural Language Processing (NLP)** project that helps students explore career paths based on their interests, strengths, skills, and preferred working style.

Instead of answering a fixed multiple-choice career quiz, users can describe themselves naturally in their own words. The system analyzes the meaning of the description and recommends the **Top 3 most semantically similar career paths**.

> **Important:** Career Discovery AI is an exploration tool, not a career prediction system. The displayed match percentage represents semantic similarity, not the probability of success in a career.

---

## Project Objective

Many students know what subjects or activities they enjoy but may not know which careers are related to those interests.

The goal of this project is to create a simple system where a student can write something like:

> "I enjoy mathematics, statistics, programming, and working with data. I like finding patterns and solving analytical problems."

The system then compares this description with a curated career knowledge base and recommends relevant career paths.

Example:

1. Data Scientist
2. Data Analyst
3. Backend Developer

---

## Main Features

- Natural-language student input
- 50 curated career profiles
- Semantic text matching
- Sentence Transformer embeddings
- Cosine similarity-based ranking
- Top 3 career recommendations
- Career descriptions
- Skills and interests
- Work-style information
- Beginner learning roadmaps
- Interactive Streamlit interface

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pandas | Data loading, cleaning, and preparation |
| NumPy | Numerical operations |
| Sentence Transformers | Generate semantic text embeddings |
| all-MiniLM-L6-v2 | Pretrained sentence embedding model |
| Scikit-learn | Cosine similarity calculation |
| Streamlit | Interactive web application |
| CSV | Career knowledge base |

---
