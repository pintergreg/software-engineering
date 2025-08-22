import squarify
import json
import matplotlib.pyplot as plt

labels = [
    "writing new code or improving existing code",
    "meetings and management",
    "code maintenance",
    "testing",
    "other",
    "security issues",
]
colors = ["#dae8fc", "#ffe6cc", "#f8cecc", "#d5e8d4", "#e1d5e7", "#fff2cc"]
sizes = [32, 23, 19, 12, 9, 4]

# these values define the coordinate system for the returned rectangles
# the values will range from x to x + width and y to y + height
x = 0.0
y = 0.0
width = 120
height = 100

# values = sizes
#
# # values must be sorted descending (and positive, obviously)
# values.sort(reverse=True)
#
# # the sum of the values must equal the total area to be laid out
# # i.e., sum(values) == width * height
# values = squarify.normalize_sizes(values, width, height)
#
# # returns a list of rectangles
# rects = squarify.squarify(values, x, y, width, height)
#
# # padded rectangles will probably visualize better for certain cases
# padded_rects = squarify.padded_squarify(values, x, y, width, height)
#
#
# with open("out.json", "w") as fp:
#     json.dump(rects, fp, indent=1)

fig, ax = plt.subplots(figsize=(6, 5), layout="constrained")
ax.set_aspect(1 / 1.2)
squarify.plot(
    sizes,
    norm_x=100,
    norm_y=100,
    color=colors,
    label=sizes,
    ax=ax,
)
ax.invert_yaxis()
# ax.axis("off")
fig.savefig("out.png")
