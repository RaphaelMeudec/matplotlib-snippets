from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import lines


output_path = Path(__file__).parent.parent / "figures" / f"{Path(__file__).stem}.png"

def get_roc_curve_samples(n_points=50):
    fpr = np.concatenate([
        [0],
        sorted(np.random.random(size=(n_points - 2,))),
        [1],
    ])
    tpr = np.concatenate([
        [0],
        sorted(np.random.random(size=(n_points - 2,))),
        [1],
    ])
    return fpr, tpr


def draw_figure(output_file=None):
    # Plot 3 ROC curves with 30 points
    for _ in range(3):
        fpr, tpr = get_roc_curve_samples(n_points=30)
        plt.plot(fpr, tpr, color="r", alpha=0.5)
    # Plot 3 ROC curves with 50 points
    for _ in range(3):
        fpr, tpr = get_roc_curve_samples(n_points=50)
        plt.plot(fpr, tpr, color="b", alpha=0.5)
    plt.legend(
        handles=[
            lines.Line2D([0], [0], color="r", label="ROC (30 points)"),
            lines.Line2D([0], [0], color="b", label="ROC (50 points)"),
        ],
        bbox_to_anchor=(1.05, 1),
    )
    plt.title(Path(__file__).stem)
    plt.tight_layout()
    if output_file:
        plt.savefig(output_file)
    else:
        plt.show()

draw_figure(output_file=output_path)


if __name__ == "__main__":
    draw_figure()
