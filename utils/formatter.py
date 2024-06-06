import mizani.labels as pl

## Axis Formaters

# plotnine
pl_k = pl.label_number(big_mark=",", scale=0.001, suffix="k", precision=0)
pl_M = pl.label_number(big_mark=",", scale=0.000001, suffix="M", precision=0)
pl_pct = pl.label_percent()

# matplotlib
fmt_M = lambda x, pos: pl_M([x])[0]
fmt_k = lambda x, pos: pl_k([x])[0]
fmt_p = lambda x, pos: f"{x:.2%}"
