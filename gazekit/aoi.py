import configparser
import os
from typing import List
import numpy as np


class AOI:
    def __init__(self, x, y, w, h, display, name, panel=None):
        assert len(display) == 2
        self.x = x/display[0]
        self.y = y/display[1]
        self.w = w/display[0]
        self.h = h/display[1]
        self.name = name
        self.panel = panel

        self.c = np.array([self.x+self.w/2, self.y+self.h/2])
        self.r = np.array([self.w/2, self.h/2])


def read_aoi_ini_file(file_path: str, display) -> List[AOI]:
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
        name = section
        p = config[section]['p'].split(',') if config[section]['p'] else []
        aoi = AOI(x, y, w, h, display, name, p)
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

