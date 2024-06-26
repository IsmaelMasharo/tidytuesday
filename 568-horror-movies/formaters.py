# %%

# https://matplotlib.org/stable/gallery/ticks/tick-formatters.html

import matplotlib.pyplot as plt
from matplotlib import ticker


def setup(ax, title):
    """Set up common parameters for the Axes in the example."""
    # only show the bottom spine
    ax.yaxis.set_major_locator(ticker.NullLocator())
    ax.spines[["left", "right", "top"]].set_visible(False)

    # define tick positions
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1.00))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.25))

    ax.xaxis.set_ticks_position("bottom")
    ax.tick_params(which="major", width=1.00, length=5)
    ax.tick_params(which="minor", width=0.75, length=2.5, labelsize=10)
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 1)
    ax.text(
        0.0,
        0.2,
        title,
        transform=ax.transAxes,
        fontsize=14,
        fontname="Monospace",
        color="tab:blue",
    )


fig = plt.figure(figsize=(8, 8), layout="constrained")
fig0, fig1, fig2 = fig.subfigures(3, height_ratios=[1.5, 1.5, 7.5])

# String Formatting
fig0.suptitle("String Formatting", fontsize=16, x=0, ha="left")
ax0 = fig0.subplots()

setup(ax0, title="'{x} km'")
ax0.xaxis.set_major_formatter("{x} km") # ----------------

# Function Formatting
fig1.suptitle("Function Formatting", fontsize=16, x=0, ha="left")
ax1 = fig1.subplots()

setup(ax1, title="def(x, pos): return str(x-5)")
ax1.xaxis.set_major_formatter(lambda x, pos: str(x - 5)) # ----------------

# Formatter Object Formatting
fig2.suptitle("Formatter Object Formatting", fontsize=16, x=0, ha="left")
axs2 = fig2.subplots(7, 1)

setup(axs2[0], title="NullFormatter()")
axs2[0].xaxis.set_major_formatter(ticker.NullFormatter()) # ----------------

setup(axs2[1], title="StrMethodFormatter('{x:.3f}')")
axs2[1].xaxis.set_major_formatter(ticker.StrMethodFormatter("{x:.3f}")) # ----------------

setup(axs2[2], title="FormatStrFormatter('#%d')")
axs2[2].xaxis.set_major_formatter(ticker.FormatStrFormatter("#%d")) # ----------------


def fmt_two_digits(x, pos):
    return f"[{x:.2f}]"

# Function Formatting
setup(axs2[3], title='FuncFormatter("[{:.2f}]".format)')
axs2[3].xaxis.set_major_formatter(ticker.FuncFormatter(fmt_two_digits)) # ----------------

# Function FixedFormatter
setup(axs2[4], title="FixedFormatter(['A', 'B', 'C', 'D', 'E', 'F'])")
# FixedFormatter should only be used together with FixedLocator.
# Otherwise, one cannot be sure where the labels will end up.
positions = [0, 1, 2, 3, 4, 5]
labels = ["A", "B", "C", "D", "E", "F"]
axs2[4].xaxis.set_major_locator(ticker.FixedLocator(positions)) 
axs2[4].xaxis.set_major_formatter(ticker.FixedFormatter(labels)) # ----------------

# Function ScalarFormatter
setup(axs2[5], title="ScalarFormatter()")
axs2[5].xaxis.set_major_formatter(ticker.ScalarFormatter(useMathText=True)) # ----------------

# Function PercentFormatter
setup(axs2[6], title="PercentFormatter(xmax=5)")
axs2[6].xaxis.set_major_formatter(ticker.PercentFormatter(xmax=5)) # ----------------

plt.show()

# %%
# also

# after plotting the data, format the labels
current_values = plt.gca().get_yticks()
# using format string '{:.0f}' here but you can choose others
plt.gca().set_yticklabels(['{:,.0%}'.format(x) for x in current_values])

# %%
# Custom formatter function
def millions_formatter(x, pos):
    if x >= 1_000_000:
        return f'{x/1_000_000:.1f}M'
    elif x >= 1_000:
        return f'{x/1_000:.1f}k'
    else:
        return str(x)

# Sample data
x = [0, 1, 2, 3, 4, 5]
y = [100, 1000, 10000, 100000, 1000000, 10000000]

# Create plot
fig, ax = plt.subplots()
ax.plot(x, y)

# Apply the formatter to the y-axis
ax.yaxis.set_major_formatter(ticker.FuncFormatter(millions_formatter))

# %%
# ------------------------------------------------------------
# MY CUSTOM FORMATERS
# ------------------------------------------------------------

fmt_M = lambda x, pos: f'{x/1_000_000:.0f}M'
fmt_k = lambda x, pos: f'{x/1_000:.0f}k'
fmt_p = lambda x, pos: f'{x:.2%}'

ax.xaxis.set_major_formatter(fmt_M)
ax.yaxis.set_major_formatter(fmt_M)