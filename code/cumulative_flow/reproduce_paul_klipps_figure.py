import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def cumulative(x: list[int]) -> list[int]:
    result = []
    k = 0
    for i in x:
        k += i
        result.append(k)
    return result


def create_half_arrow(
    startx: float,
    starty: float,
    endx: float,
    endy: float,
    scale: int = 65,
    color: str = "#962212",
) -> mpatches.FancyArrowPatch:
    return mpatches.FancyArrowPatch(
        (startx, starty),
        (endx, endy),
        arrowstyle="simple",
        mutation_scale=scale,
        color=color,
    )


if __name__ == "__main__":
    output = "../../lectures/figures"

    deployed = [0, 0, 0, 1, 3, 6, 8, 12, 14]
    ready_for_approval = [0, 0, 1, 2, 2, 1, 2, 1, 0]
    in_testing = [0, 1, 2, 2, 2, 2, 2, 1, 0]
    in_progress = [1, 2, 2, 2, 1, 2, 1, 0, 0]
    ready_to_start = [5, 5, 5, 4, 4, 2, 1, 0, 0]

    fig, ax = plt.subplots(figsize=(9, 6), layout="constrained")
    ax.stackplot(
        range(9),
        deployed,
        ready_for_approval,
        in_testing,
        in_progress,
        ready_to_start,
        labels=[
            "deployed",
            "ready for approval",
            "in testing",
            "in progress",
            "ready to start",
        ],
        colors=["#4c70a8", "#87b664", "#e9b257", "#c04a42", "#895e9d"],
    )
    ax.add_patch(create_half_arrow(2, 6, 5, 6, scale=75))
    ax.add_patch(create_half_arrow(3, 6, 0, 6, scale=75))
    ax.text(
        2.5,
        6,
        "lead time",
        ha="center",
        va="center",
        size=12,
        color="white",
    )

    ax.add_patch(create_half_arrow(1.5, 3, 3, 3))
    ax.add_patch(create_half_arrow(2.5, 3, 1, 3))
    ax.text(
        2,
        3,
        "cycle time",
        ha="center",
        va="center",
        size=12,
        color="white",
    )

    ax.add_patch(create_half_arrow(4, 9, 4, 12))
    ax.add_patch(create_half_arrow(4, 10, 4, 8))
    ax.text(
        4,
        10,
        "backlog size",
        ha="center",
        va="center",
        size=12,
        color="white",
        rotation=270,
    )

    ax.add_patch(create_half_arrow(5, 8, 5, 11))
    ax.add_patch(create_half_arrow(5, 9, 5, 6))
    ax.text(
        5,
        8.5,
        "work in progress",
        ha="center",
        va="center",
        size=12,
        color="white",
        rotation=270,
    )

    ax.add_patch(create_half_arrow(6, 10, 6, 14))
    ax.add_patch(create_half_arrow(6, 11, 6, 8))
    ax.text(
        6,
        11,
        "remaining to be done",
        ha="center",
        va="center",
        size=12,
        color="white",
        rotation=270,
    )

    ax.add_patch(create_half_arrow(1, 10, 1, 14))
    ax.add_patch(create_half_arrow(1, 11, 1, 8))
    ax.text(
        1,
        11,
        "remaining to be done",
        ha="center",
        va="center",
        size=12,
        color="white",
        rotation=270,
    )
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(
        handles[::-1],
        labels[::-1],
        ncols=5,
        loc="lower center",
        bbox_to_anchor=(0.5, -0.175),
    )
    ax.margins(0)
    ax.set_xlabel("days", fontsize=14)
    ax.set_ylabel("number of tasks", fontsize=14)
    fig.savefig(f"{output}/cdf.svg", dpi=300, pad_inches=0.1, bbox_inches="tight")
