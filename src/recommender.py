# import pandas as pd
# from pathlib import Path

# from sentence_transformers import SentenceTransformer
# from sklearn.metrics.pairwise import cosine_similarity

# # DEFINE FILE PATH

# BASE_DIR = Path(__file__).resolve().parent.parent

# DATA_FILE = BASE_DIR / "data" / "careers_prepared.csv"


# # LOAD CAREER DATA

# print("Loading career dataset...")

# df = pd.read_csv(DATA_FILE)

# print(f"Loaded {len(df)} careers.")


# # LOAD SENTENCE TRANSFORMER MODEL

# print("Loading sentence embedding model...")

# model = SentenceTransformer("all-MiniLM-L6-v2")

# print("Model loaded successfully!")


# # GENERATE CAREER EMBEDDINGS

# print("Generating career embeddings...")

# career_texts = df["career_text"].tolist()

# career_embeddings = model.encode(
#     career_texts,
#     normalize_embeddings=True
# )

# print(f"Career embeddings created: {career_embeddings.shape}")


# # CREATE RECOMMENDATION FUNCTION

# def recommend_careers(student_text, top_n=3):

#     # Remove unnecessary spaces
#     student_text = student_text.strip()

#     # Check if the student entered anything
#     if not student_text:
#         return []

#     # Convert student description into an embedding
#     student_embedding = model.encode(
#     [student_text],
#     normalize_embeddings=True
#     )

#     # Compare student embedding with all career embeddings
#     similarities = cosine_similarity(
#         student_embedding,
#         career_embeddings
#     )[0]

#     # Create a copy of the dataset
#     results = df.copy()

#     # Add similarity score
#     results["similarity"] = similarities

#     # Sort careers from highest similarity to lowest
#     results = results.sort_values(
#         by="similarity",
#         ascending=False
#     )

#     # Select the top results

#     results = results.head(top_n)

#     return results

# # TEST THE RECOMMENDER WHEN THIS FILE IS RUN DIRECTLY

# if __name__ == "__main__":

#     example_student = """
# I enjoy communicating with people, organizing teams,
# solving business problems and planning projects.
# I like leadership, strategy and making decisions.
# """

#     print("\nStudent Description:")
#     print(example_student)

#     recommendations = recommend_careers(
#         example_student,
#         top_n=3
#     )

#     print("\n--- TOP CAREER MATCHES ---")

#     for rank, (_, row) in enumerate(
#         recommendations.iterrows(),
#         start=1
#     ):

#         match_score = row["similarity"] * 100

#         print(
#             f"\n{rank}. {row['career']}"
#         )

#         print(
#             f"Category: {row['category']}"
#         )

#         print(
#             f"Match Score: {match_score:.2f}%"
#         )

#         print(
#             f"Description: {row['description']}"
#         )



import pandas as pd
from pathlib import Path

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# 1. DEFINE FILE PATH

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "careers_prepared.csv"


# 2. LOAD CAREER DATA

print("Loading career dataset...")

df = pd.read_csv(DATA_FILE)

print(f"Loaded {len(df)} careers.")


# 3. LOAD SENTENCE TRANSFORMER MODEL

print("Loading sentence embedding model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

print("Model loaded successfully!")


# 4. CREATE CAREER MATCH EMBEDDINGS

print("Generating career embeddings...")

career_match_texts = df["match_text"].tolist()

career_embeddings = model.encode(
    career_match_texts,
    normalize_embeddings=True
)

print(
    f"Career embeddings created: "
    f"{career_embeddings.shape}"
)


# 5. RECOMMENDATION FUNCTION

def recommend_careers(student_text, top_n=3):

    # Clean user input
    student_text = student_text.strip()

    # Handle empty input
    if not student_text:
        return pd.DataFrame()

    # Create student embedding
    student_embedding = model.encode(
        [student_text],
        normalize_embeddings=True
    )

    # Calculate cosine similarity
    similarities = cosine_similarity(
        student_embedding,
        career_embeddings
    )[0]

    # Copy career dataset
    results = df.copy()

    # Add similarity scores
    results["similarity"] = similarities

    # Sort highest to lowest
    results = results.sort_values(
        by="similarity",
        ascending=False
    )

    # Return top careers
    return results.head(top_n)


# 6. TEST THE RECOMMENDER

if __name__ == "__main__":

    # example_student = """
    # I enjoy communicating with people, organizing teams,
    # solving business problems and planning projects.
    # I like leadership, strategy and making decisions.
    # """

#     example_student = """
# I enjoy mathematics, statistics and working with data.
# I like finding patterns, analyzing information,
# using Python and creating useful insights from numbers.
# """

    example_student = """
I enjoy creativity, visual design and understanding
how people use websites and mobile applications.
I like designing interfaces, creating prototypes
and improving user experience.
"""

#     example_student = """
# I enjoy programming and solving logical problems.
# I like building software applications, debugging code,
# working with computers and learning new technologies.
# """

#     example_student = """
# I enjoy social media, creating online content,
# understanding audiences and promoting brands.
# I like creativity, marketing campaigns and
# communicating with people online.
# """
#     long_student = """
# I enjoy mathematics and solving logical problems.
# I have started learning Python and I also enjoy working
# with spreadsheets and analyzing information. I like
# understanding why things happen and finding patterns.
# At the same time, I enjoy communicating my findings
# to other people and creating charts or visual reports.
# I prefer structured work but also enjoy learning new
# technology and solving practical business problems.
# """

    print("\nStudent Description:")
    print(example_student)

    recommendations = recommend_careers(
        example_student,
        top_n=3
    )

    # print(long_student)

    # recommendations = recommend_careers(
    # long_student,
    # top_n=3
    # )
    
    print("\n--- TOP CAREER MATCHES ---")

    for rank, (_, row) in enumerate(
        recommendations.iterrows(),
        start=1
    ):

        match_score = row["similarity"] * 100

        print(f"\n{rank}. {row['career']}")
        print(f"   Category: {row['category']}")
        print(
            f"   Match Score: "
            f"{match_score:.2f}%"
        )
        print(
            f"   Description: "
            f"{row['description']}"
        )