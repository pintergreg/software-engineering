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
ax.set_facecolor("none")
fig.set_facecolor("none")
sns.barplot(
    versions.sort_values("date", ascending=True),
    x="date",
    y="lines",
    ax=ax,
    color="#FFE6CC",
)
for patch, ver in zip(
    ax.patches, versions.sort_values("date", ascending=True)["release"]
):
    patch.set_edgecolor("#D79B00")
    patch.get_x()
    ax.text(
        patch.get_x() + patch.get_width() / 2,
        2,
        f"Firefox {ver}",
        ha="center",
        va="bottom",
        rotation=90,
        color="#D79B00",
        fontsize=12,
        fontweight="bold",
    )

ax.set_ylabel("million lines of code", fontsize=14)
ax.set_xlabel("")

fig.autofmt_xdate()
for i in ["png", "svg"]:
    fig.savefig(f"firefox_codebase_growth.{i}")
