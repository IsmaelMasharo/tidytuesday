import random
import pandas as pd


# %%
def year_major_category_sample():
    # Create a list of major categories
    major_categories = [
        "Engineering",
        "Business",
        "Health",
        "Education",
        "Computer Science",
    ]

    # Create a list of years from 2011 to 2020
    years = list(range(2011, 2021))

    # Create an empty list to store the data
    data = []

    # Generate random data for each combination of major category and year
    for category in major_categories:
        for year in years:
            # Generate a random number of graduate students
            graduate_students = random.randint(100, 1000)

            # Generate a random major based on the major category
            if category == "Engineering":
                major = random.choice(
                    [
                        "Mechanical Engineering",
                        "Electrical Engineering",
                        "Civil Engineering",
                    ]
                )
            elif category == "Business":
                major = random.choice(["Finance", "Marketing", "Management"])
            elif category == "Health":
                major = random.choice(["Nursing", "Pharmacy", "Physical Therapy"])
            elif category == "Education":
                major = random.choice(
                    ["Elementary Education", "Secondary Education", "Special Education"]
                )
            elif category == "Computer Science":
                major = random.choice(
                    ["Computer Programming", "Data Science", "Artificial Intelligence"]
                )
            else:
                major = "Unknown"

            # Append the data to the list
            data.append(
                {
                    "Major_category": category,
                    "Year": year,
                    "Graduate_students": graduate_students,
                    "Major": major,
                }
            )

    # Convert the list of dictionaries to a DataFrame
    df_sample = pd.DataFrame(data)

    return df_sample


# %%
