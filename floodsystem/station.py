# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""

from typing import Tuple

class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d
    
    def typical_range_consistent(self):
        """Checks to see if the Monitoring Station checked has a valid result for its high/low range data"""
        return type(self.typical_range) is tuple

def check_stations_input(stations):
    """This function checks the stations input for another fuction

    Args:
        stations (list): list of MonitoringStation objects

    Raises:
        Exception: If the input is not a list
        Exception: If one of the items in the list is not a MonitoringStation object

    Returns:
        boolean: True if it passes all the tests, else an Exception
    """
    if type(stations) is not list: raise Exception("Input variable is not a list")
    for item in stations:
        if type(item) is not MonitoringStation:
            raise Exception(f"The variable, {item}, for the list imported is of type {type(item)} and not of type MonitoringStation")
    return True

def check_coordinate(p):
    """Checks that the input is of the correct type for a coordinate

    Args:
        p (tulpe): (longitude,latitude)

    Raises:
        Exception: If it 

    Returns:
        boolean: True if it passes all tests, else an Exception
    """
    if type(p) is not tuple:
            raise Exception(f"{p} is of invalid co-ordinate of type {type(p)}, but it should be a tuple")
    if len(p) != 2:
        raise Exception(f"{p} is a tuple but of invalid length of {len(p)}, but it should be 2")
    if (type(p[0]) is not float and type(p[0]) is not int) or (type(p[1]) is not float and type(p[1]) is not int):
        raise Exception(f"{p} is the correct type and length, but it should be made of floats or ints to represent the long and lat")
    return True

def inconsistent_typical_range_stations(stations):
    """Given a list of station objects, this returns a list of stations that have inconsistent data for the high/low argument

    Args:
        stations (list): list of stations
    """
    check_stations_input(stations)
    
    returnList = []
    for MonitoringStation in stations:
        if MonitoringStation.typical_range_consistent() == False:
            returnList.append(MonitoringStation)
    return returnList
