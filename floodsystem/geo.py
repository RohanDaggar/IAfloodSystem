# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from turtle import st
from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit
from math import sqrt
from floodsystem.station import MonitoringStation


def stations_by_distance(stations, p):
    station_and_distance = []
    for station in stations:
        distance = haversine(station.coord, p)
        station_and_distance.append([station.name, station.town, distance])
    return sorted_by_key(station_and_distance, 2)

def stations_within_radius(stations, centre, r):
    """Prints an alphabetic list of the stations within a radius 'r' around a centre 'centre'

    Args:
        stations (list): list of the stations using the station class
        centre (tuple): centre co-ordinate descibed in a tuple (x,y)
        r (integer): radius r given in km
    """
    
    less_than_10 = []
    for station in stations:
        distance = haversine(station.coord, centre)
        if distance <= r:
               less_than_10.append(station.name)
    return less_than_10

def rivers_with_station(stations):
    river_station = set()
    for station in stations:
        river_station.add(station.river)
    return sorted(river_station)

def stations_by_river(stations):
    """Maps river names to a list of station objects

    Args:
        stations (list): list of MonitoringStation objects

    Returns:
        dictionary: the key is the river and the item is a list of stations at that river
    """
    d_stations_river = {}
    for station in stations:
        if station.river in d_stations_river:
            d_stations_river[station.river].append(station.name)
            d_stations_river[station.river].sort()
        else:
            d_stations_river[station.river] = [station.name]
    
    return d_stations_river

def rivers_by_station_number(stations, N):
    """This determins N rivers with the greatest number of monitoring stations.
    In the case that there are more rivers with the same number of stations as the N th entry, this includes these rivers in the list.

    Args:
        stations (list): list of MonitoringStation objects
        N (int): number of rivers
    """
    assert type(N) is int
    assert type(stations) is list
    assert N >= 1
    
    river_stations = stations_by_river(stations)
    river_numbers = []
    for key in river_stations:
        river_numbers.append((key,len(river_stations[key])))
    river_numbers_s = sorted_by_key(river_numbers, 1, True)
    
    while river_numbers_s[N-1][1] == river_numbers_s[N][1]:
        N += 1
    
    
    return river_numbers_s[:N]
    