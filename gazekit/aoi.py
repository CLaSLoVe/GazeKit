import configparser
import os
from typing import List
import numpy as np


class Display:
    def __int__(self, w, h):
        self.w = w
        self.h = h
        self.area = w * h


class AOI:
    def __init__(self, x, y, w, h, name=None, panel=None, display=None):
        assert (type(display) == Display) or (display is None)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.name = name
        self.panel = panel
        self.area = w * h

        self.c = np.array([x+w/2, y+h/2])
        self.r = np.array([w/2, h/2])

        if display:
            self.area_ratio = w * h / display.area


def read_aoi_ini_file(file_path: str, display=None) -> List[AOI]:
    if not os.path.isfile(file_path):
        raise FileNotFoundError("No [aoi].ini file!")
    # read ini
    config = configparser.ConfigParser()
    config.read(file_path)

    aois: List[AOI] = []
    for section in config.sections():
        x = int(config[section]['x'])
        y = int(config[section]['y'])
        w = int(config[section]['w'])
        h = int(config[section]['h'])
        name = config[section]['name']
        function = config[section]['function'].split(',') if config[section]['function'] else []
        aoi = AOI(x, y, w, h, name, function, display)
        aois.append(aoi)
    return aois


def xy2aoi(xy, centers, radius):
    aois = []
    for i in range(len(centers)):
        center = centers[i]
        radiu = radius[i]
        in_set = (np.abs(xy - center) < radiu)
        dist_xy = np.logical_and.reduce(in_set.T, axis=0)
        aois.append(dist_xy)
    return np.array(aois).T

if __name__ == '__main__':
    xy = np.array([[2,2],[2,3],[2,4]])
    centers = np.array([[5,2],[2,3]])
    radius = np.array([[10,.5],[.5,.5]])
    print(xy2aoi(xy, centers, radius))

