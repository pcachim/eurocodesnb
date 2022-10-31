
import numpy as np


def calc_parabola(x1, y1, x2, y2, x3, y3, nump=20):
    '''
    Adapted and modifed to get the unknowns for defining a parabola:
    http://stackoverflow.com/questions/717762/how-to-calculate-the-vertex-of-a-parabola-given-three-points
    '''

    denom = (x1-x2) * (x1-x3) * (x2-x3);
    a     = (x3 * (y2-y1) + x2 * (y1-y3) + x1 * (y3-y2)) / denom;
    b     = (x3*x3 * (y1-y2) + x2*x2 * (y3-y1) + x1*x1 * (y2-y3)) / denom;
    c     = (x2 * x3 * (x2-x3) * y1+x3 * x1 * (x3-x1) * y2+x1 * x2 * (x1-x2) * y3) / denom;

    #Define x range for which to calc parabola
    x_pos=np.linspace(x1, x3, nump)
    y_pos = (a*x_pos+b)*x_pos+c

    return x_pos, y_pos