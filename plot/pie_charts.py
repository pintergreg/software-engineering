import matplotlib.pyplot as plt
import numpy as np

data = [20, 80]
colors = ["#ffffde", "#f1f1ff"]
explode = [0.1, 0]
labels = ["used", "not used"]
for i, a in enumerate([90, 30, 120, 180, 300]):
    fig, ax = plt.subplots(
        figsize=(5, 5), dpi=120, layout="constrained", facecolor="none"
    )
    wedges, _ = ax.pie(
        data,
        colors=colors,
        # autopct="%1.0f%%",
        labels=None,
        startangle=a,
        wedgeprops={"edgecolor": "#2d2d2d", "linewidth": 2},
        explode=explode,
    )
    for wedge, lab in zip(wedges, labels):
        theta = np.deg2rad((wedge.theta1 + wedge.theta2) / 2)  # middle angle
        r = 0.6  # radius where text is placed (0 to 1)
        x, y = r * np.cos(theta), r * np.sin(theta)
        ax.text(
            x,
            y,
            lab,
            ha="center",
            va="center",
            fontsize=24,
            color="#2d2d2d",
        )
    ax.axis("equal")  # keeps the pie chart circular
    fig.savefig(f"../lectures/figures/pie/{i}.svg", bbox_inches="tight")
