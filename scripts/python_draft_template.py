"""
Minimal SpotPaper template for Python-first dataviz drafts.

Replace placeholder values with paper-specific numbers and labels.
Keep the structure explicit and easy to edit.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


OUTPUT = Path("outputs/spotpaper_draft.png")


def draw_composition_shift():
    labels = ["Group A", "Group B"]
    top_values = [20, 80]
    bottom_values = [65, 35]

    fig, ax = plt.subplots(figsize=(6, 8))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    top_y0, top_y1 = 0.82, 0.94
    bottom_y0, bottom_y1 = 0.08, 0.20

    top_total = sum(top_values)
    bottom_total = sum(bottom_values)

    top_edges = [0.15]
    for value in top_values:
        top_edges.append(top_edges[-1] + 0.70 * value / top_total)

    bottom_edges = [0.15]
    for value in bottom_values:
        bottom_edges.append(bottom_edges[-1] + 0.70 * value / bottom_total)

    colors = ["#D55C4B", "#D9D9D9"]

    for i, label in enumerate(labels):
        ax.fill_between(
            [top_edges[i], top_edges[i + 1]],
            top_y0,
            top_y1,
            color=colors[i],
            linewidth=0,
        )
        ax.fill_between(
            [bottom_edges[i], bottom_edges[i + 1]],
            bottom_y0,
            bottom_y1,
            color=colors[i],
            linewidth=0,
        )

        poly = Polygon(
            [
                (top_edges[i], top_y0),
                (top_edges[i + 1], top_y0),
                (bottom_edges[i + 1], bottom_y1),
                (bottom_edges[i], bottom_y1),
            ],
            closed=True,
            facecolor=colors[i],
            alpha=0.45,
            edgecolor="none",
        )
        ax.add_patch(poly)

        ax.text((top_edges[i] + top_edges[i + 1]) / 2, top_y1 + 0.02, f"{label}\n{top_values[i]}%", ha="center", va="bottom", fontsize=10)
        ax.text((bottom_edges[i] + bottom_edges[i + 1]) / 2, bottom_y0 - 0.03, f"{label}\n{bottom_values[i]}%", ha="center", va="top", fontsize=10)

    ax.text(0.5, 0.98, "Baseline composition", ha="center", va="top", fontsize=12, fontweight="bold")
    ax.text(0.5, 0.50, "Policy-shaped entry / reweighting", ha="center", va="center", fontsize=11)
    ax.text(0.5, 0.02, "Output composition", ha="center", va="bottom", fontsize=12, fontweight="bold")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT, dpi=200, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    draw_composition_shift()
