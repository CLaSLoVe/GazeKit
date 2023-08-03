class Display:
    def __int__(self, w, h):
        self.w = w
        self.h = h
        self.area = w*h


class AOI:
    def __init__(self, x, y, w, h, name=None, function=None, display=None):
        assert type(display) == Display
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.name = name
        self.function = function
        self.area = w*h

        if display:
            self.area_ratio = w*h/display.area



