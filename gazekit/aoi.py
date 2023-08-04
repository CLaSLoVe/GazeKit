import configparser
import os
from typing import List
import numpy as np


class AOI:
    def __init__(self, x, y, w, h, name, display=(1, 1), panel=None):
        """
        Initializes an AOI (Area of Interest) object.

        :param x: The x-coordinate of the top-left corner of the AOI in pixels.
        :param y: The y-coordinate of the top-left corner of the AOI in pixels.
        :param w: The width of the AOI in pixels.
        :param h: The height of the AOI in pixels.
        :param name: The name of the AOI.
        :param display: The display dimensions in pixels, represented as (width, height).
        :param panel: The specific functionality of the AOI, represented as a list.
        :raises AssertionError: If the length of the `display` tuple is not 2.

        """
        assert len(display) == 2, "The display tuple must have exactly 2 elements."
        self.x = x / display[0]
        self.y = y / display[1]
        self.w = w / display[0]
        self.h = h / display[1]
        self.name = name
        self.panel = panel

        self.c = np.array([self.x + self.w / 2, self.y + self.h / 2])
        self.r = np.array([self.w / 2, self.h / 2])


def xy2aoi(xy: np.ndarray, centers: list, radius: list) -> np.ndarray:
    """
    Converts a set of XY coordinates to AOIs (Areas of Interest) based on specified centers and radii.

    :param xy: An array of XY coordinates.
    :type xy: numpy.ndarray
    :param centers: A list of center coordinates for each AOI.
    :type centers: list
    :param radius: A list of radii for each AOI.
    :type radius: list
    :return: An array representing the AOIs where each column corresponds to an AOI and each row corresponds to a coordinate in `xy`.
    :rtype: numpy.ndarray
    """
    aois = []

    for i in range(len(centers)):
        center = centers[i]
        radiu = radius[i]
        in_set = np.abs(xy - center) < radiu
        dist_xy = np.logical_and.reduce(in_set.T, axis=0)
        aois.append(dist_xy)

    return np.array(aois).T


def read_aoi_ini_file(file_path: str, display) -> List[AOI]:
    """
    Read an AOI (.ini) file and return a list of AOI objects.

    :param file_path: the path to the AOI (.ini) file.
    :type file_path: str
    :param display: the display object to use for converting coordinates from pixels to degrees of visual angle.
    :type display: Display
    :return: a list of AOI objects representing the areas of interest defined in the AOI file.
    :rtype: list[AOI]
    :raises FileNotFoundError: if the AOI file specified by `file_path` does not exist.
    """

    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Could not find file: {file_path}")
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
        aoi = AOI(x, y, w, h, name, display, p)
        aois.append(aoi)
    return aois


if __name__ == '__main__':
    xy = np.array([[2,2],[2,3],[2,4]])
    centers = np.array([[5,2],[2,3]])
    radius = np.array([[10,.5],[.5,.5]])
    print(xy2aoi(xy, centers, radius))

