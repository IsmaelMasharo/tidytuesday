# %%
import pandas as pd

# %%
path = "data/538-college-mayor-economic-guide.csv"
df = pd.read_csv(path)
df = df[["Major_category", "Major", "Total"]]


# %%
def fct_reorder(df, factor, agg_by, agg_funct="median"):
    """
    Adds category ordering to a dataframe based on aggregated values of another column.\n
    It does not reorder the dataframe, but it changes the category order of the factor column.\n
    Helpfull for plotting functions that use the category order to sort the plot.
    """

    # Aggregate values for each category
    agg_category = df.groupby(factor, observed=True)[agg_by].agg(agg_funct)

    # Get the order of the categories sorted by the aggregated values
    category_order = agg_category.sort_values().index

    # Create a categorical dtype with categories sorted by mean values
    category_dtype = pd.CategoricalDtype(categories=category_order, ordered=True)

    # Assign the new category order to the 'category' column
    df[factor] = df[factor].astype(category_dtype)

    return df


# %%
df_fct_ordered = fct_reorder(df, "Major_category", "Total")

# %%
# tiene el parametro by y lo utiliza para ordenar las categorias
df_fct_ordered.boxplot(column="Total", by="Major_category", vert=False)

# %%
# tiene el parametro by pero no lo utiliza para ordenar las categorias
df_fct_ordered.plot(kind="box", column="Total", by="Major_category", vert=False)

# aca se ve que tiene el parametro by, ya que si no lo pongo plotea el Total
df_fct_ordered.plot(kind="box", column="Total", vert=False)

# %%
# tiene el parametro by pero no lo utiliza para ordenar las categorias
df_fct_ordered.plot.box(column="Total", by="Major_category", vert=False)

# %%
df_fct_ordered.sort_values(["Major_category", "Total"]).plot.box(
    column="Total", by="Major_category", vert=False
)

# %%
df_fct_ordered.sort_values(["Major_category", "Total"]).reset_index(drop=True).plot(
    kind="box", column="Total", by="Major_category", vert=False
)

# %%
df_fct_ordered.sort_values(["Major_category", "Total"], ascending=False).reset_index(
    drop=True
).plot(kind="box", column="Total", by="Major_category", vert=False)

# %%
# creo que lo ideal es no depender de orden por categoria sino ordenar el dataframe directamente con sort
# ni siquiera asi, acabo de probar 2 arriba y tampoco funciona haciendo el sorting, parece que es un bug en la implementacion de pandas, porque solo respeta el orden con .boxplot y no con plot.box ni plot(kind='box')

# parece que matplotlib no tiene esa forma para ordenar, solo ordena todas las columnas en el orden que aparecen

# segun la documentacion de pandas
"""
by: str or array-like, optional
Column in the DataFrame to pandas.DataFrame.groupby(). One box-plot will be done per value of columns in by.

return_type: {‘axes’, ‘dict’, ‘both’} or None, default ‘axes’
The kind of object to return. The default is axes.

‘axes’ returns the matplotlib axes the boxplot is drawn on.

‘dict’ returns a dictionary whose values are the matplotlib Lines of the boxplot.

‘both’ returns a namedtuple with the axes and dict.

when grouping with by, a Series mapping columns to return_type is returned.

If return_type is None, a NumPy array of axes with the same shape as layout is returned.
"""

# ese by esta usando pandas groupby internamente, matplolib no tiene eso por defecto

# ya se por que puede ser, groupby tiene un parametro llamado sort, que ordena los grupos (no los records, sino los grupos). Parece que solo el metodo boxplot, que usa by->groupby, tiene ese parametro set to True. en el resto parece que no porque en la documentacion de pandas groupby dice que hacer sort=True implica mayores recursos, y facil esta usando el nuevo default de sort=False. entonces cual es el default grouping de pandas? supuestamente es en base a las ocurrencias, pero ya le hice sorting arriba y ni asi ordeno el boxplot, ni siquiera haciendo un reindex

# la pregunta sigue, como hace pandas el grouping?
"""
sort:
Changed in version 2.0.0: Specifying sort=False with an ordered categorical grouper will no longer sort the values.
"""
# Esa documentacion parece un error, parece que debio ser sort=True, o sort en general, con variables categorias no lo va a ordenar?
# O tal vez quiere decir que si la variable categorica ya esta ordenada, el sort=False pues no la va a desordenar, o sea no va a ordenarla.
