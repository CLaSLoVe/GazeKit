import numpy as np
import pandas as pd
import warnings

from denoise import *
from aoi import *
from tools import *

class Sequence:
    def __init__(self, x, y, t, d=None, aoi=None, history=None):
        """
        Create a new `Sequence` object to represent eye-tracking data.

        :param x: array of x-coordinates of eye positions.
        :type x: array-like
        :param y: array of y-coordinates of eye positions.
        :type y: array-like
        :param t: array of timestamps of eye positions, relative to the start of the recording.
        :type t: array-like
        :param d: array of durations of eye movements, or `None` if not available.
        :type d: array-like or None
        :param aoi: array of area-of-interest information for each eye position, or `None` if not available.
                    If provided, this should be a list of `AOI` objects representing the areas of interest.
        :type aoi: array-like or None
        :param history: list of strings representing the processing history of the `Sequence` object, or `None` if not
                        available.
        :type history: list[str] or None
        """
        if len(x) == 0:
            raise ValueError("Cannot create Sequence object with empty x array.")
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
        """
        Locate areas of interest (AOIs) in the eye-tracking data.

        :param aoi_list: a list of `AOI` objects representing the areas of interest to locate.
        :type aoi_list: list[AOI]
        """
        self.aoi_list = aoi_list
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
        self.data['aoi_encode'] = encode_bool_lists(aoi_array)
        for i, aoi in enumerate(aoi_list):
            self.data[aoi.name] = aoi_array[:, i]

    def detect_fixations(self, min_duration=0.1, max_dispersion=0.0004):
        """Detect fixations from eye-tracking data."""
        # Compute distance between consecutive eye positions
        self.info.append('detect_fixations')

        dx = np.diff(self.data['x'])
        dy = np.diff(self.data['y'])
        dist = np.sqrt(dx ** 2 + dy ** 2)

        ...

    def denoise(self, func, **kwargs):
        """
        Denoise eye-tracking data using a specified function.

        :param func: function to use for denoising. This function should take a `Sequence` object as its first argument,
                     and any additional keyword arguments passed to `denoise` should be passed to `func`.
        :type func: function
        :param **kwargs: keyword arguments to pass to the denoising function `func`.
        :type **kwargs: dict
        :return: denoised `Sequence` object.
        :rtype: Sequence
        """
        pack = [self.data[col].values for col in self.data.columns]
        self.info.append('denoise with'+func.__name__)
        return func(self, **kwargs)

    def plot(self, func, **kwargs):
        """
        Plot eye-tracking data.

        :param func: function to use for plotting. This function should take a `Sequence` object as its first argument,
                     and any additional keyword arguments passed to `plot` should be passed to `func`.
        :type func: function
        :param **kwargs: keyword arguments to pass to the plotting function `func`.
        :type **kwargs: dict
        """


if __name__ == '__main__':
    data = np.genfromtxt('../tests/data.csv', delimiter=',', dtype=None, encoding=None)
    aois = read_aoi_ini_file('../tests/aoi.ini', (2560, 1600))
    seq = Sequence(*data.T)
    seq.loc_aoi(aois)
    # seq_d = seq.denoise(XXXMethod, window_size=5, polyorder=3)
    # seq_f = seq_d.detect_fixations()

