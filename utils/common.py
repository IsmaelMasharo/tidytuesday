import pandas as pd
import numpy as np
import re

# Matplotlib format axis
fmt_M = lambda x, pos: f"{x/1_000_000:.0f}M"
fmt_k = lambda x, pos: f"{x/1_000:.0f}k"


def fct_reorder(df, factor, agg_by, agg_funct="median"):
    """
    Adds category ordering to a dataframe based on aggregated values of another column.\n
    It does not reorder the dataframe, but it changes the category order of the factor column.\n
    Helpfull for plotting functions that use the category order to sort the plot (df.boxplot()).\n
    Returns the factor columns with its new categorical type without mutating the original df
    """

    # when using .index on a series or a df that has a CategoricalIndex it returns the actual type of CategoricalIndex that has info related to the order or not of the CategoricalIndex. When passed directly to pd.CategoricalDtype and ordered=True it will take the actual categorical values order. that why i'm getting an error when the factor argument is already a pd.CategoricalDtype in step 3. It is not assiging new categorical order but taking the already existing order. To fix it i had to call .index.tolist() to remove the information of the previous CategoricalIndex if any.

    # 1. Aggregate values for each category
    agg_category = df.groupby(factor, observed=True)[agg_by].agg(agg_funct)

    # 2. Get the order of the categories sorted by the aggregated values. FIXED
    category_order = agg_category.sort_values().index.tolist()

    # 3. Create a categorical dtype with categories sorted by mean values
    category_dtype = pd.CategoricalDtype(categories=category_order, ordered=True)

    # Assign the new category order to the 'category' column
    return df[factor].astype(category_dtype)


def fct_lump_n(df, column_name, n):
    # TODO: account for nan values in the column

    # Get the value counts of the categories
    category_counts = df[column_name].value_counts()

    # Get the top n categories
    top_categories = category_counts[:n].index.tolist()

    # Replace all other categories with a new category called "Other"
    return np.where(df[column_name].isin(top_categories), df[column_name], "Other")


def remove_unicode(df):
    # Function to remove non-ASCII characters
    def remove_non_ascii(text):
        return re.sub(r"[^\x00-\x7F]+", "", text)

    # Remove non-ASCII characters from all text columns
    for col in df.select_dtypes(include=["object"]).columns:
        df[col] = df[col].apply(
            lambda x: remove_non_ascii(x) if isinstance(x, str) else x
        )
