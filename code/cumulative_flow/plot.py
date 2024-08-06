import matplotlib.pyplot as plt


def cumulative(x: list[int]) -> list[int]:
    result = []
    k = 0
    for i in x:
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
