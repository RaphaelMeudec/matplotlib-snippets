from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


output_path = Path(__file__).parent.parent / "figures" / f"{Path(__file__).stem}.png"


def draw_figure(output_file=None):
    # Instantiate some data
    X = np.arange(60)
    Y = 2 * X + 5 * np.random.random((len(X),))

    # Draw simple figure
    plt.figure()
    plt.plot(X, Y)

    # Customize our ticks
    ax = plt.gca()
    # Set our tick positions and labels
    ax.set_xticks([5, 15, 25, 35, 45, 55])
    # Those label can be considerer as years for the example
    ax.set_xticklabels([1900, 1920, 1940, 1960, 1980, 2000])
    # Start customizing our ticks
    ticks = plt.xticks()

    # Example 1: century years should be in green, others in red
    for (tick_index, tick_text) in zip(*ticks):
        is_century = int(tick_text.get_text()) % 100 == 0
        color = "green" if is_century else "red"
        tick_text.set_color(color)

    # Example 2: leap years should be in bold (only 1900 isn't a leap year)
    for (tick_index, tick_text) in zip(*ticks):
        year = int(tick_text.get_text())
        is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        fontweight = "bold" if is_leap_year else "normal"
        tick_text.set_fontweight(fontweight)

    plt.title(Path(__file__).stem)
    if output_file:
        plt.savefig(output_file)
    else:
        plt.show()

draw_figure(output_file=output_path)


if __name__ == "__main__":
    draw_figure()
