import squarify
import json
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import yaml

mpl.rcParams["svg.hashsalt"] = "42"

with open("plotting_config.yaml", "r") as fp:
    config = yaml.safe_load(fp)


labels = [
    "writing new code\nor improving existing code",
    "meetings and management",
    "code maintenance",
    "testing",
    "other",
    "security issues",
]
colors = ["#dae8fc", "#ffe6cc", "#f8cecc", "#d5e8d4", "#e1d5e7", "#fff2cc"]
edge_colors = ["#dae8fc", "#ffe6cc", "#f8cecc", "#d5e8d4", "#e1d5e7", "#fff2cc"]
sizes = [32, 23, 19, 12, 10, 4]

legend_elements = []
for label, color, edge in zip(labels, colors, edge_colors):
    elem = Patch(fc=color, ec=edge, label=label)
    legend_elements.append(elem)

fig, ax = plt.subplots(figsize=(6, 5), layout="constrained", dpi=150)
fig.set_facecolor("none")
# ax.set_aspect(1 / 1.2)
ax.set_aspect("equal")
squarify.plot(
    sizes,
    norm_x=100,
    norm_y=100,
    color=colors,
    # label=sizes,
    ax=ax,
)
ax.invert_yaxis()
legend = ax.legend(
    handles=legend_elements,
    ncols=1,
    fontsize=12,
    loc="upper right",
    bbox_to_anchor=(1.9375, 1),
)
legend.get_frame().set_alpha(None)

# positions = [(5, 5), (5, 64), (60, 5), (60, 48), (60, 75), (90, 75)]
positions = [(3, 3), (3, 62), (58, 3), (58, 46), (58, 73), (89, 73)]
for pos, s in zip(positions, sizes):
    ax.text(pos[0], pos[1], f"{s}", ha="left", va="top", fontsize=28)
ax.axis("off")
for i in config["formats"]:
    fig.savefig(
        f"../lectures/figures/how_developers_spend_time.{i}",
        metadata=config["metadata"][i],
        bbox_inches="tight",
    )
