import matplotlib.pyplot as plt

output = "../../lectures/figures"
colors = ["#110F0E", "#673821", "#BD9931", "#EEE436", "#E9E9DC"][1:]
colors = [
    "#EBCF2E",
    "#B4BF3A",
    "#88AB38",
    "#5E9432",
    "#3B7D31",
    "#225F2F",
    "#244422",
    "#252916",
][::-2]

days = range(1, 6)

done = [0, 10, 40, 42, 45]
review = [0, 12, 35, 10, 15]
doing = [25, 30, 20, 20, 20]
todo = [40, 35, 30, 15, 20]

fig, ax = plt.subplots(figsize=(6, 4), layout="constrained")
ax.stackplot(
    days,
    done,
    review,
    doing,
    todo,
    labels=["done", "review", "doing", "todo"],
    colors=colors,
)
handles, labels = ax.get_legend_handles_labels()
ax.legend(
    # handles[::-1],
    # labels[::-1],
    ncols=4,
    loc="upper left",
)
ax.margins(0)
# ax.set_xlabel("days")
ax.set_ylim([0, 150])
ax.set_xticks([])
ax.set_yticks([])
# fig.savefig(f"{output}/cumulative_flow_diagram.svg", dpi=300, pad_inches=0.1)
fig.savefig("bn.svg", dpi=300, pad_inches=0)
