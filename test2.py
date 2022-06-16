import numpy as np
import matplotlib.pyplot as plt


def main():
    h = 10 / np.sqrt(2 * np.pi)
    d = 100
    c = 2500
    x_dots = list(range(0, 4016, 1))
    y_dots = [h * np.exp(-(np.square((x - c) / d)) / 2) for x in x_dots]

    fig, ax = plt.subplots()
    ax.plot(x_dots, y_dots)
    plt.show()


if __name__ == "__main__":
    main()
