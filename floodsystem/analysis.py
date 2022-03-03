import numpy as np
#import matplotlib
from matplotlib.dates import date2num

def polyfit(dates, levels, p):
    
    time = date2num(dates)
    d0 = time[0]
    
    p_coeff = np.polyfit(time-d0, levels, p)
    poly = np.poly1d(p_coeff)
    
    return poly, d0
    