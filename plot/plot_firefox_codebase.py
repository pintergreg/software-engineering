import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

versions = pd.read_csv("data/firefox/firefox_versions.csv", nrows=11)
versions["date"] = pd.to_datetime(versions["date"], format="%Y-%m-%d")

result = {}
for i in versions["release"].tolist():
    data = pd.read_csv(
        f"data/firefox/ff{i}.txt",
        sep=r"\s{2,}",
        engine="python",
        skiprows=3,
        skipfooter=3,
        names=["language", "files", "lines", "code", "comments", "blanks"],
    )
    result[i] = int(data["lines"].sum())

versions["lines"] = result.values()
versions["lines"] = round(versions["lines"] / 1000000, 2)

fig, ax = plt.subplots(figsize=(6, 5), layout="constrained", dpi=150)
# ax.bar(list(result.keys()), list(result.values()))
sns.barplot(
    versions.sort_values("date", ascending=True),
    x="date",
    y="lines",
    ax=ax,
    # color="#DAE8FC",
    color="#FFE6CC",
)
for patch in ax.patches:
    # patch.set_edgecolor("#6C8EBF")
    patch.set_edgecolor("#D79B00")
ax.set_ylabel("million lines of code", fontsize=14)
ax.set_xlabel("")


# xlabels = ["{:,.2f}".format(x) + "K" for x in g.get_xticks() / 1000]
# g.set_xticklabels(xlabels)
fig.autofmt_xdate()
for i in ["png", "svg"]:
    fig.savefig(f"firefox_codebase_growth.{i}")
