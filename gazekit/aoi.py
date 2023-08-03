import configparser
import os
from typing import List


class Display:
    def __int__(self, w, h):
        self.w = w
        self.h = h
        self.area = w * h


class AOI:
    def __init__(self, x, y, w, h, name=None, function=None, display=None):
        assert (type(display) == Display) or (display is None)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.name = name
        self.function = function
        self.area = w * h

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
