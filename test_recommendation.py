# {
#  "cells": [],
#  "metadata": {
#   "language_info": {
#    "name": "python"
#   }
#  },
#  "nbformat": 4,
#  "nbformat_minor": 5
# }

from src.recommender import recommend_careers

# TEST STUDENT PROFILES

test_students = [

    {
        "name": "Data-Focused Student",
        "description": """
        I enjoy mathematics, statistics and working with data.
        I like finding patterns, analyzing information,
        using Python and creating useful insights from numbers.
        """
    },

    {
        "name": "Programming-Focused Student",
        "description": """
        I enjoy programming and solving logical problems.
        I like building software applications, debugging code,
        working with computers and learning new technologies.
        """
    },

    {
        "name": "Design-Focused Student",
        "description": """
        I enjoy creativity, visual design and understanding
        how people use websites and mobile applications.
        I like designing interfaces, creating prototypes
        and improving user experience.
        """
    },

    {
        "name": "Business-Focused Student",
        "description": """
        I enjoy communicating with people, organizing teams,
        solving business problems and planning projects.
        I like leadership, strategy and making decisions.
        """
    },

    {
        "name": "Marketing-Focused Student",
        "description": """
        I enjoy social media, creating online content,
        understanding audiences and promoting brands.
        I like creativity, marketing campaigns and
        communicating with people online.
        """
    },

    {
        "name": "Mixed Business and Technology Student",
        "description": """
        I enjoy technology but I also like communicating
        with people and solving business problems.
        I am interested in understanding users,
        planning products and working with technical teams.
        """
    },

    # {
    #     "name": "Empty Input Student",
    #     "description": ""
    # },

    # {
    #     "name": "Very Short Input Student",
    #     "description": "I like computers."
    # }

]

# RUN ALL TESTS

print("\n========================================")
print("CAREER DISCOVERY AI - TESTING")
print("========================================")


for student in test_students:

    print("\n\n----------------------------------------")
    print(student["name"])
    print("----------------------------------------")

    print("\nStudent Description:")
    print(student["description"].strip())

    recommendations = recommend_careers(
        student["description"],
        top_n=3
    )

    print("\nTop 3 Career Matches:")

    for rank, (_, row) in enumerate(
        recommendations.iterrows(),
        start=1
    ):

        match_score = row["similarity"] * 100

        print(
            f"\n{rank}. {row['career']}"
        )

        print(
            f"   Category: {row['category']}"
        )

        print(
            f"   Match Score: {match_score:.2f}%"
        )

# TEST EMPTY INPUT

print("\n\n----------------------------------------")
print("Empty Input Test")
print("----------------------------------------")

empty_result = recommend_careers("")

if empty_result.empty:
    print("PASS: Empty input returned no recommendations.")
else:
    print("FAIL: Empty input should not return recommendations.")


# TEST VERY SHORT INPUT

print("\n\n----------------------------------------")
print("Very Short Input Test")
print("----------------------------------------")

short_result = recommend_careers(
    "I like computers.",
    top_n=3
)

print("\nResults for very short input:")

for rank, (_, row) in enumerate(
    short_result.iterrows(),
    start=1
):

    match_score = row["similarity"] * 100

    print(
        f"{rank}. {row['career']} "
        f"- {match_score:.2f}%"
    )


print("\n\n========================================")
print("TESTING COMPLETE")
print("========================================")