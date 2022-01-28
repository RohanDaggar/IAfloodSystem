# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit
from math import sqrt


def stations_within_radius(stations, centre, r):
    """Prints an alphabetic list of the stations within a radius 'r' around a centre 'centre'

    Args:
        stations (list): list of the stations using the station class
        centre (tuple): centre co-ordinate descibed in a tuple (x,y)
        r (integer): radius r given in km
    """
    
    less_than_10 = []
    for stations in stations:
        distance = haversine(station.coord, centre)
        if distance <= r:
               less_than_10.append(station.name)
    return less_than_10