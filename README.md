# Career Discovery AI - Project

## Career Discovery AI

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

## How It Works

```text
Career Dataset
      ↓
Data Preparation
      ↓
Career Match Profiles
      ↓
Sentence Embeddings
      ↓
Student Description → Student Embedding
      ↓
Cosine Similarity
      ↓
Rank 50 Careers
      ↓
Top 3 Career Matches
      ↓
Streamlit Application
```
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

## Project Structure

```text
career-discovery-ai/
│
├── data/
│   ├── careers.csv
│   └── careers_prepared.csv
│
├── src/
│   ├── prepare_data.py
│   ├── recommender.py
│   └── test_embeddings.py
│
├── app.py
├── test_recommendation.py
└── requirements.txt
```
### Main Files

- **`careers.csv`** – Original dataset containing 50 career profiles.
- **`prepare_data.py`** – Cleans the data and creates `career_text` and `match_text`.
- **`careers_prepared.csv`** – Prepared dataset used for matching.
- **`test_embeddings.py`** – Tests the Sentence Transformer embeddings.
- **`recommender.py`** – Generates embeddings, calculates cosine similarity, and returns the Top 3 careers.
- **`test_recommendation.py`** – Tests different student profiles and edge cases.
- **`app.py`** – Final Streamlit user interface.
---  

## Recommendation Logic

The project uses the pretrained **all-MiniLM-L6-v2** Sentence Transformer.

Each career profile and student description is converted into a **384-dimensional embedding**.

```text
Student Description → 384-D Embedding
                         ↓
                  Cosine Similarity
                         ↑
Career match_text → 384-D Embeddings
                         ↓
                 Top 3 Careers
```
The model is **pretrained**; this project uses it for inference rather than training a new neural network.

---

## Development Journey

The recommendation system went through three approaches:

### 1. `career_text`
Initially, career description, skills, interests, and work style were combined into one profile.
The system worked technically, but some recommendations were not logically strong.

### 2. Weighted Matching
Separate similarities were tested using:

```text
Interests       35%
Skills          25%
Description     25%
Work Style      15%
```
This improved some results but remained inconsistent.

### 3. `match_text` – Final Approach
The main problem was **data representation**.
`career_text` described **what a career is**, while student input described **what the student enjoys**.
Therefore, `match_text` was created to describe **what kind of student may enjoy each career**.
This produced better recommendations while keeping the final algorithm simple.

---

## Testing

The final system was tested with different profiles:

| Student Profile | Top Recommendation |
|---|---|
| Data-focused | Data Scientist |
| Programming-focused | Software Engineer |
| Design-focused | UI/UX Designer |
| Business-focused | Project Manager |
| Marketing-focused | Social Media Manager |

Empty, very short, and mixed-interest inputs were also tested.

---

## Run the Project

Activate the virtual environment:

```bash
source .venv/bin/activate
```
Install dependencies:
```bash
pip install -r requirements.txt
```
Prepare the dataset:
```bash
python src/prepare_data.py
```
Test embeddings:
```bash
python src/test_embeddings.py
```
Run the recommendation engine:
```bash
python src/recommender.py
```
Run all recommendation tests:
```bash
python test_recommendation.py
```
Run the final application:
```bash
streamlit run app.py
```
---

## Key Learning

The main learning from this project was that **better data representation can be more important than increasing algorithm complexity**.
Changing from `career_text` to `match_text` improved the recommendations without requiring a more complicated model.

---

## Limitations

- Currently limited to 50 careers
- Results depend on the quality of student input
- Similar careers may overlap semantically
- Does not consider academic performance or job-market data
- Provides career exploration, not career prediction
---

**Omi Chaurasia**

This is my 4 Day Workshop project covering data preparation, NLP, machine learning, recommendation logic, testing, and application development.

## Thank You!
