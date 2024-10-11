import matplotlib.pyplot as plt


def n(x: int) -> int:
    return (x * (x - 1)) / 2


if __name__ == "__main__":
    colors = [
        "#FED789",
        "#023743",
        "#72874E",
        "#476F84",
        "#A4BED5",
        "#453947",
    ]
    output = "../../lectures/figures"
    x = range(3, 13)
    y = [n(i) for i in range(3, 13)]
    fig, ax = plt.subplots(figsize=(6, 6), layout="constrained")
    ax.fill_between(x, y, color=colors[1])
    # ax.plot(x, y, color=colors[1], lw=3, marker="o", markersize=10)
    # ax.set_xlim([2.75, 12.25])
    ax.set_ylim([0, None])
    ax.set_xlabel("number of people in the team")
    ax.set_ylabel("communication channels")
    ax.margins(0)
    fig.savefig(
        f"{output}/communication_overhead.svg",
        dpi=300,
        pad_inches=0.1,
    )
