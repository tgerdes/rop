from opc.colors import *
from opc.matrix import OPCMatrix
from opc.hue import getHueGen

from math import sin, cos, pi, fabs
from utils.frange import frange

DELTA_Z = 0.05

class Art:

    description = "Lissajous figures"

    def __init__(self, matrix):
        self.hue = getHueGen(0.01)
        self.phase_z = 0

    def start(self, matrix):
        matrix.clear()

    def refresh(self, matrix):
        matrix.shift(.9, 1, .9)
        self.phase_z += DELTA_Z

        color = self.hue.next()
        xcenter = matrix.width/2.0
        ycenter = matrix.height/2.0
        theta = sin(self.phase_z)
        if theta < 0:
            theta_x, theta_y = 1, 1 - 2*theta
        else:
            theta_x, theta_y = 1 + 2*theta, 1

        for angle in frange(0, 2*pi, 0.01):
            x = xcenter + xcenter * sin(theta_x * angle)
            y = ycenter + ycenter * cos(theta_y * angle)
            matrix.drawPixel(x, y, color)
        
    def interval(self):
        return 100

