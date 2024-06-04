import mizani.labels as pl

## Axis Formaters

# plotnine
pl_k = pl.label_currency(big_mark=",", scale=0.001, suffix="k", precision=0)
pl_M = pl.label_currency(big_mark=",", scale=0.000001, suffix="M", precision=0)

# matplotlib
fmt_M = lambda x, pos: pl_M(x)
fmt_k = lambda x, pos: pl_k(x)
fmt_p = lambda x, pos: f"{x:.2%}"
