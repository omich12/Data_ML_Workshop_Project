import pandas as pd
from pathlib import Path

# DEFINE FILE PATHS

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "data" / "careers.csv"
OUTPUT_FILE = BASE_DIR / "data" / "careers_prepared.csv"


# LOAD THE DATASET

print("Loading career dataset...")

df = pd.read_csv(INPUT_FILE)

print("Dataset loaded successfully!")


# CHECK BASIC DATASET INFORMATION

print("\n--- DATASET INFORMATION ---")

print(f"Number of careers: {len(df)}")
print(f"Number of columns: {len(df.columns)}")

print("\nColumns:")
print(df.columns.tolist())

print("\nMissing values before cleaning:")
print(df.isnull().sum())


# HANDLE MISSING TEXT VALUES

text_columns = [
    "career",
    "category",
    "description",
    "skills",
    "interests",
    "work_style",
    "roadmap"
]

for column in text_columns:
    df[column] = df[column].fillna("").astype(str).str.strip() # three small cleaning operations


# CREATE A COMBINED CAREER PROFILE

df["career_text"] = (
    "Career: " + df["career"] + ". "
    + "Description: " + df["description"] + ". "
    + "Skills: " + df["skills"] + ". "
    + "Interests: " + df["interests"] + ". "
    + "Work style: " + df["work_style"] + "."
)

# CREATE A MATCHING PROFILE FOR EACH CAREER

df["match_text"] = (
    "A student who may enjoy a career as "
    + df["career"]
    + " may be interested in "
    + df["interests"]
    + ". They may enjoy using skills such as "
    + df["skills"]
    + ". The work may suit someone who prefers "
    + df["work_style"]
    + ". The career involves "
    + df["description"]
    + "."
)

# CHECK THE PREPARED DATA

print("\n--- AFTER DATA PREPARATION ---")

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nExample prepared career:")
print(df.loc[0, "career"])

print("\nCombined career text:")
print(df.loc[0, "career_text"])


# SAVE THE PREPARED DATASET

df.to_csv(OUTPUT_FILE, index=False)

print("\nPrepared dataset saved successfully!")
print(f"Saved to: {OUTPUT_FILE}")

print(f"\nFinal dataset shape: {df.shape}")
