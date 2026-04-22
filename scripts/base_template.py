"""
Minimal SpotPaper template for quick-read Python-first dataviz drafts.

Replace placeholder values with paper-specific numbers and labels.
Keep the structure explicit and easy to edit.

Template defaults:
- one dominant central comparison
- a claim-style headline rather than a neutral chart title
- generous outer margins with tighter internal spacing
- a large main subplot that carries the first-glance message
- no white background panel for the main subplot
- short, noun-style comparison labels
- optional scope line between the main structure and the metric row
- optional secondary metrics shown as a weak, unboxed metric row
- secondary metrics must not outrank the main comparison
- upper and lower sections should share the same horizontal alignment logic
- no source note inside the figure by default
- no bbox_inches="tight" by default
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


OUTPUT = Path("outputs/base_template_preview.png")


def add_metric(ax, x_center, heading, value, symbol="", accent="#8b4d2d"):
    ax.text(
        x_center,
        0.74,
        heading,
        ha="center",
        va="center",
        fontsize=12.2,
        fontweight="bold",
        color="#5d554d",
        transform=ax.transAxes,
    )
    ax.text(
        x_center,
        0.44,
        value,
        ha="center",
        va="center",
        fontsize=22,
        fontweight="bold",
        color=accent,
        transform=ax.transAxes,
    )
    if symbol:
        ax.text(
            x_center + 0.10,
            0.44,
            symbol,
            ha="center",
            va="center",
            fontsize=16,
            color=accent,
            transform=ax.transAxes,
        )


def draw_central_comparison():
    left_title = "Baseline"
    right_title = "Access"
    left_share = 0.20
    right_share = 0.65
    scope_label = "Focal group"

    fig = plt.figure(figsize=(10.8, 8.2), facecolor="#f7f1e6")
    gs = fig.add_gridspec(100, 100, left=0.05, right=0.95, top=0.95, bottom=0.05)

    # Default composition:
    # - generous outer margins
    # - larger central comparison area
    # - optional, weak metric row below
    top = fig.add_subplot(gs[12:69, 10:90])
    bottom = fig.add_subplot(gs[76:95, 10:90])
    top.set_facecolor("none")
    bottom.set_facecolor("none")
    top.set_xlim(0, 1)
    top.set_ylim(0, 1)
    top.set_xticks([])
    top.set_yticks([])
    top.axis("off")
    bottom.axis("off")

    fig.text(
        0.10,
        0.91,
        "A Small Base Captures Most Access",
        fontsize=24,
        fontweight="bold",
        color="#2a2a2a",
    )

    favored = "#2f79b7"
    neutral = "#d9d0c2"
    text = "#2a2a2a"
    accent = "#8b4d2d"

    # Main comparison should dominate the figure.
    # Keep bar centers and lower metric centers on the same shared grid.
    bar_x = [0.19, 0.66]
    bar_w = 0.14
    bar_h = 0.70
    bar_y = 0.12
    centers = [x + bar_w / 2 for x in bar_x]

    top.text(
        centers[0],
        0.87,
        left_title,
        ha="center",
        va="center",
        fontsize=13,
        color=text,
        fontweight="bold",
    )
    top.text(
        centers[1],
        0.87,
        right_title,
        ha="center",
        va="center",
        fontsize=13,
        color=text,
        fontweight="bold",
    )

    for x in bar_x:
        top.add_patch(Rectangle((x, bar_y), bar_w, bar_h, linewidth=1.0, edgecolor="#cbbfae", facecolor=neutral))

    top.add_patch(Rectangle((bar_x[0], bar_y), bar_w, bar_h * left_share, linewidth=0, facecolor=favored))
    top.add_patch(Rectangle((bar_x[1], bar_y), bar_w, bar_h * right_share, linewidth=0, facecolor=favored))

    top.text(
        centers[0],
        bar_y + bar_h * left_share / 2,
        f"{int(left_share * 100)}%",
        ha="center",
        va="center",
        fontsize=20,
        color="white",
        fontweight="bold",
    )
    top.text(
        centers[1],
        bar_y + bar_h * right_share / 2,
        f"{int(right_share * 100)}%",
        ha="center",
        va="center",
        fontsize=22,
        color="white",
        fontweight="bold",
    )

    # Keep connector treatment weak; the main bars should carry the message.
    top.annotate(
        "",
        xy=(0.61, 0.50),
        xytext=(0.39, 0.50),
        arrowprops=dict(arrowstyle="-|>", lw=1.6, color="#c96f56"),
    )
    top.text(
        0.50,
        0.56,
        "access",
        ha="center",
        va="center",
        fontsize=10.5,
        color="#8a7c70",
    )

    # Optional scope line for cases where the focal group needs to be made explicit.
    # Prefer this over a floating side label or an isolated callout box.
    fig.text(0.50, 0.27, scope_label, ha="center", va="center", fontsize=12.6, fontweight="bold", color=favored)

    # Optional secondary metric row.
    # Keep these weaker than the main bars, smaller than the main percentages,
    # and use at most one metric per side.
    add_metric(bottom, centers[0], "timing", "75 days", "↓", accent=accent)
    add_metric(bottom, centers[1], "valuation", "12%", "↗", accent=accent)

    fig.text(0.965, 0.03, "generated by SpotPaper", fontsize=8.8, color="#a9a29a", ha="right")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT, dpi=200, facecolor=fig.get_facecolor())
    plt.close(fig)


if __name__ == "__main__":
    draw_central_comparison()
