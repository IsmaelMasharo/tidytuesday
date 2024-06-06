### General Exploration Process

- find tops x across y. top 20 earnings across majors
- plot to see distribution of variables, distributions of summaries (dist of median)
- make counts and weighted sums. exmp: count(Major_category), count(Major_category by Total) = agg(major and sum its weights ) . Weighted count is only the name dyplr gives to that operation, not generally used in statistics. The process is actully suming the weights of each category ~~~
- how much do college graduates earn in general (histogram of salaries)
- are the high income salaries an acquate representation of the income one could expect from a major or is just due to **small sample size**
- comparing distribution by using boxplot, sorting one propertie to better see trends
- does this factor explain a lot of the variation, the outcome. 'exposure' -> 'outcome'
- look at the outliers
- more sample size, check if there is less variation, it should i think, if not one should take into account sample ~~~ if there is more variation in the low sample sizes than in the high sample sizes ...

### Plots
- When using plotnine in a jupyter notebook, matplotlib plots don't show anymore, and when using plt.show() they appear double plots. A configuration with plotnine seems to be causing this. A menos que se plotee primero uno que no sea plotnine.
- [Matplotlib formatting axis](https://jakevdp.github.io/PythonDataScienceHandbook/04.10-customizing-ticks.html)