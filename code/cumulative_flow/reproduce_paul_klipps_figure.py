import matplotlib.pyplot as plt


def cumulative(x: list[int]) -> list[int]:
    result = []
    k = 0
    for i in x:
        k += i
        result.append(k)
    return result


if __name__ == "__main__":
    output = "../../lectures/figures"

    deployed = [0, 0, 0, 1, 3, 6, 8, 12, 14]
    ready_for_approval = [0, 0, 1, 2, 2, 1, 2, 1, 0]
    in_testing = [0, 1, 2, 2, 2, 2, 2, 1, 0]
    in_progress = [1, 2, 2, 2, 1, 2, 1, 0, 0]
    ready_to_start = [5, 5, 5, 4, 4, 2, 1, 0, 0]

    fig, ax = plt.subplots(figsize=(6, 4), layout="constrained")
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
    ax.margins(0)
    fig.savefig(f"{output}/cdf.svg", dpi=300, pad_inches=0.1)
