from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


output_path = Path(__file__).parent.parent / "figures" / f"{Path(__file__).stem}.png"


def draw_figure(output_file=None):
    # Instantiate some data with 3 gaussians around 1, 10 and 100
    X = np.concatenate([
        np.random.random(size=(500,)),
        10 * np.random.random(size=(500,)) + 10,
        100 * np.random.random(size=(500,)) + 100,
    ])

    n_bins = 50
    plt.figure()
    plt.gca().set_xscale("log")
    # The trick is to set the bins not using a raw integer but instead use np.geomspace
    hist, bins, _ = plt.hist(
        X,
        bins=np.geomspace(X.min(), X.max(), num=n_bins),
    )

    plt.title(Path(__file__).stem)
    if output_file:
        plt.savefig(output_file)
    else:
        plt.show()


draw_figure(output_file=output_path)


if __name__ == "__main__":
    draw_figure()
