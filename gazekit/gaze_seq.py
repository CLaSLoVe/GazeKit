import numpy as np
import pandas as pd


class Sequence:
    def __init__(self, x, y, t):
        eye = {'x': x,
               'y': y,
               'raw_t': t,
               'rel_t': np.array(t) - t[0]}
        self.data = pd.DataFrame(eye)


if __name__ == '__main__':
    data = np.genfromtxt('../tests/data.csv', delimiter=',', dtype=None, encoding=None)
    x, y, t = data[:, 0], data[:, 1], data[:, 2]
    seq = Sequence(x, y, t)
