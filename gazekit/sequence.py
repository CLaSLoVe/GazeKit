import numpy as np
import pandas as pd
from denoise import *
from aoi import *
import warnings
from tools import *

class Sequence:
    def __init__(self, x, y, t, d=None, aoi=None, history=None):
        assert x[0], "Empty sequence."
        data = {'x': x,
                'y': y,
                't': np.array(t) - t[0]}
        if d is not None:
            data['duration'] = d
        if aoi is not None:
            data['aoi'] = aoi
        self.data = pd.DataFrame(data)

        # record process history
        if history:
            self.info = history
        else:
            self.info = []

    def __call__(self, *args, **kwargs):
        return self.data

    def loc_aoi(self, aoi_list):
        if 'aoi' in self.data.columns:
            warnings.warn("exist AOI will be replaced!", UserWarning)
        centers = []
        radius = []
        for aoi in aoi_list:
            centers.append(aoi.c)
            radius.append(aoi.r)
        xy = seq.data[['x', 'y']].to_numpy()
        centers = np.array(centers)
        radius = np.array(radius)
        aoi_array = xy2aoi(xy, centers, radius)
        self.data['aoi'] = encode_bool_lists(aoi_array)

    def detect_fixations(self, min_duration=0.1, max_dispersion=0.0004):
        """Detect fixations from eye-tracking data."""
        # Compute distance between consecutive eye positions
        self.info.append('detect_fixations')

        dx = np.diff(self.data['x'])
        dy = np.diff(self.data['y'])
        dist = np.sqrt(dx ** 2 + dy ** 2)

        ...

    def denoise(self, func, **kwargs):
        """Denoise eye-tracking data"""
        pack = [self.data[col].values for col in self.data.columns]
        self.info.append('denoise with'+func.__name__)
        return func(self, **kwargs)

    def plot(self, func, **kwargs):
        ...


if __name__ == '__main__':
    data = np.genfromtxt('../tests/data.csv', delimiter=',', dtype=None, encoding=None)
    aois = read_aoi_ini_file('../tests/aoi.ini', (2560, 1600))
    seq = Sequence(*data.T)
    seq.loc_aoi(aois)
    # seq_d = seq.denoise(XXXMethod, window_size=5, polyorder=3)
    # seq_f = seq_d.detect_fixations()

