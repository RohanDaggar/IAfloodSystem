# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from turtle import st
from .utils import sorted_by_key  # noqa
from haversine import haversine
from math import sqrt
from floodsystem.station import MonitoringStation, check_stations_input


def stations_by_distance(stations, p):
    """This function generates a list of stations with their
    corresponding distances to a coordinate, p

    Args:
        stations (list): list of MonitoringStation objects
        p (tuple): a point in the form (longitude,latitude)

    Returns:
        list: a sorted by distance list of tuples in the form (station, distance from p) where station is
              a MonitoringStation object and distance from p is a float
    """
    #the checks for the inputs into this function
    check_stations_input(stations)
    assert type(p) is tuple
    
    station_and_distance = []
    for station in stations:
        #some error checks are done here
        if type(station.coord) is not tuple:
            raise TypeError(f"Station: {station}\n has an invalid co-ordinate of type {type(station.coord)}, but it should be a tuple")
        if len(station.coord) != 2:
            raise TypeError(f"Station: {station}\n is a tuple but of invalid length of {len(station.coord)}, but it should be 2")
        if type(station.coord[0]) is not float or type(station.coord[1]) is not float:
            raise TypeError(f"Station: {station}\n has an invalid long/lat: {station.coord}, but it should be a float")
        
        distance = haversine(station.coord, p)
        station_and_distance.append([station, distance])
    return sorted_by_key(station_and_distance, 1)

def stations_within_radius(stations, centre, r):
    """Prints an alphabetic list of the stations within a radius 'r' around
    a centre 'centre'

    Args:
        stations (list): list of MonitoringStation objects
        centre (tuple): centre co-ordinate descibed in a tuple (longitude,latitude)
        r (integer): radius r given in km
        
    Returns:
        list: Station names within a distance r from point p
    """
    #the checks for the inputs into this function
    check_stations_input(stations)
    assert type(r) is int
    assert type(centre) is tuple and len(centre) == 2
               
    distance_list = stations_by_distance(stations, centre)
    stations_within_distance = []
    for station in distance_list:
        if station[1] < r:
            #stations_within_distance.append(station[0])
            stations_within_distance.append(station)
    return stations_within_distance

def rivers_with_station(stations):
    """returns a list of all the rivers contained within the list of stations

    Args:
        stations (list): list of MonitoringStation objects

    Returns:
        list: a list of rivers with at least one station
    """
    #the checks for the inputs into this function
    check_stations_input(stations)
    
    river_station = set() 
    for station in stations:
        river_station.add(station.river)
    return sorted(river_station)

def stations_by_river(stations):
    """groups stations by the same river together

    Args:
        stations (list): list of MonitoringStation objects

    Returns:
        dictionary: maps the river as the key to a list of MonitoringStation objects
    """
    #the checks for the inputs into this function
    check_stations_input(stations)
    
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
    In the case that there are more rivers with the same number of
    stations as the N th entry, this includes these rivers in the list.

    Args:
        stations (list): list of MonitoringStation objects
        N (int): number of rivers to return
        
    Returns:
        list: each element is a tuple in the form (river name, number of stations by the river)
            it is sorted from the highest number of stations down, and stations with the same number of stations are
            sorted alphabetically
    """
    #the checks for the inputs into this function
    assert type(N) is int and N >= 1
    check_stations_input(stations)

    river_stations = stations_by_river(stations)
    
    river_numbers = []
    for key in river_stations:
        river_numbers.append((key,len(river_stations[key])))
    river_numbers_s = sorted_by_key(river_numbers, 1, True)
    
    #this makes it so rivers with the same number of stations are also all included
    #it also makes sure not to over iterate
    try:
        while river_numbers_s[N-1][1] == river_numbers_s[N][1]:
            N += 1
    except IndexError:
        if N > len(river_numbers):
            print(f"Input N of {N} is greater than the list of rivers of length {len(river_numbers)}, so all the rivers are being returned")
        else:
            print("Max rivers reached, returning all values")
        return river_numbers_s
    
    return river_numbers_s[:N]
    