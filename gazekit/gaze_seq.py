import numpy as np
import pandas as pd
from denoise import *


class Sequence:
    def __init__(self, x, y, t, d=None):
        assert x[0], "Empty sequence."
        data = {'x': x,
                'y': y,
                't': np.array(t) - t[0]}
        if d is not None:
            data['duration'] = d
        self.data = pd.DataFrame(data)

    def __call__(self, *args, **kwargs):
        return self.data

    def detect_fixations(self, min_duration=0.1, max_dispersion=0.0004):
        """Detect fixations from eye-tracking data."""
        # Compute distance between consecutive eye positions
        dx = np.diff(self.data['x'])
        dy = np.diff(self.data['y'])
        dist = np.sqrt(dx ** 2 + dy ** 2)

        ...

    def XXXMethod(self, window_size=5, polyorder=3):
        """Denoise eye-tracking data"""
        pack = self.data[0], self.data[1], self.data[2]
        return Sequence(XXXMethod(*pack, window_size, polyorder))

    ...


if __name__ == '__main__':
    data = np.genfromtxt('../tests/data.csv', delimiter=',', dtype=None, encoding=None)
    x, y, t = data[:, 0], data[:, 1], data[:, 2]
    seq = Sequence(x, y, t)
    seq_d = seq.XXXMethod()
    seq_f = seq_d.detect_fixations()
