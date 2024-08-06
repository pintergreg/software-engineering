import matplotlib.pyplot as plt


def cumulative(x: list[int]) -> list[int]:
    result = []
    k = 0
    for i in daily_completed:
        k += i
        result.append(k)
    return result


output = "../../lectures/figures"

daily_completed = [0, 0, 1, 0, 2, 3, 0, 1, 1, 3, 2, 4, 5, 4]
days = range(1, 15)
backlog = [26]

inprogress = [5, 5, 4, 4, 2, 1] + [0] * 8
testing___ = [0, 0, 1, 1, 0, 2, 5, 5] + [0] * 6
done = cumulative(daily_completed)
# testing = cumulative(testing)

fig, ax = plt.subplots(figsize=(6, 4), layout="constrained")
# ax.fill_between(days, done)
# ax.fill_between(days, inprogress)
ax.stackplot(days, done, inprogress)
ax.margins(0)
fig.savefig(f"{output}/cumulative_flow_diagram.svg", dpi=300, pad_inches=0.1)


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
