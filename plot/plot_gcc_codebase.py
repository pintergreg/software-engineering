import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import yaml
import matplotlib as mpl

mpl.rcParams["svg.hashsalt"] = "42"

with open("plotting_config.yaml", "r") as fp:
    config = yaml.safe_load(fp)

versions = pd.read_csv("data/gcc/versions.csv", nrows=13).query(
    "~release.str.endswith('2')"
)
versions["date"] = pd.to_datetime(versions["date"], format="%B %d %Y")


result = {}
for i in versions["release"].tolist():
    ver = i.replace(".", "_").replace("GCC ", "")
    data = pd.read_csv(
        f"data/gcc/gcc_{ver}.txt",
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
    color="#E1D5E7",
)
for patch, ver in zip(
    ax.patches, versions.sort_values("date", ascending=True)["release"]
):
    patch.set_edgecolor("#9673A6")
    patch.get_x()
    ax.text(
        patch.get_x() + patch.get_width() / 2,
        2,
        f"{ver}",
        ha="center",
        va="bottom",
        rotation=90,
        color="#9673A6",
        fontsize=12,
        fontweight="bold",
    )

ax.set_ylabel("million lines of code", fontsize=14, fontweight="bold")
ax.set_yticks(ax.get_yticks())
ax.set_yticklabels(ax.get_yticklabels(), weight="bold")
ax.set_xlabel("")
ax.set_ylim([0, 17])
ax.set_xticks(ax.get_xticks())
ax.set_xticklabels(ax.get_xticklabels(), weight="bold")

fig.autofmt_xdate()
for i in config["formats"]:
    fig.savefig(
        f"../lectures/figures/gcc_codebase_growth.{i}",
        metadata=config["metadata"][i],
    )
