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
    plt.rcParams["text.usetex"] = True
    output = "../../lectures/figures"
    x = range(3, 13)
    y = [n(i) for i in range(3, 13)]
    fig, ax = plt.subplots(figsize=(4, 4), layout="constrained")
    ax.fill_between(x, y, color=colors[1])
    ax.set_ylim([0, None])
    ax.set_xlabel("number of people in the team", fontsize=14)
    ax.set_ylabel("communication channels", fontsize=14)
    ax.text(7, 50, r"$\frac{n(n-1)}{2}$", ha="center", fontsize=40)
    ax.margins(0)
    fig.savefig(
        f"{output}/communication_overhead_eq.svg",
        dpi=300,
        pad_inches=0.1,
        metadata={"Creator": "Gergő Pintér", "Date": None},
    )
    plt.show()
