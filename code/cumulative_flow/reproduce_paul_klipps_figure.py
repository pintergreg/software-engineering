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

    dep = [0, 0, 0, 1, 3, 6, 8, 12, 14]
    rfa = [0, 0, 1, 2, 2, 1, 2, 1, 0]
    ite = [0, 1, 2, 2, 2, 2, 2, 1, 0]
    inp = [1, 2, 2, 2, 1, 2, 1, 0, 0]
    rts = [5, 5, 5, 4, 4, 2, 1, 0, 0]

    fig, ax = plt.subplots(figsize=(6, 4), layout="constrained")
    ax.stackplot(
        range(9),
        dep,
        rfa,
        ite,
        inp,
        rts,
        labels=[
            "deployed",
            "ready to approval",
            "in testing",
            "in progress",
            "ready to start",
        ],
        colors=["#4c70a8", "#87b664", "#e9b257", "#c04a42", "#895e9d"],
    )
    ax.margins(0)
    fig.savefig(f"{output}/cdf.svg", dpi=300, pad_inches=0.1)
