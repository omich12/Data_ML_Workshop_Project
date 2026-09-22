import pandas as pd
from pathlib import Path
from sentence_transformers import SentenceTransformer


# FIND THE PROJECT FOLDER

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_FILE = BASE_DIR / "data" / "careers_prepared.csv"


# LOAD THE PREPARED CAREER DATA

print("Loading prepared career dataset...")

df = pd.read_csv(DATA_FILE)

print("Dataset loaded!")
print(f"Number of careers: {len(df)}")


# LOAD THE SENTENCE TRANSFORMER MODEL

print("\nLoading sentence embedding model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

print("Model loaded successfully!")


# GET THE CAREER TEXT

career_texts = df["career_text"].tolist()

print("\nExample career:")
print(df.loc[0, "career"])

print("\nExample career text:")
print(career_texts[0])


# GENERATE EMBEDDINGS

print("\nGenerating career embeddings...")

career_embeddings = model.encode(career_texts)

print("Embeddings created successfully!")


# CHECK EMBEDDING SIZE

print("\nEmbedding matrix shape:")
print(career_embeddings.shape)

print("\nFirst career embedding shape:")
print(career_embeddings[0].shape)

print("\nFirst 10 numbers of the first career embedding:")
print(career_embeddings[0][:10])