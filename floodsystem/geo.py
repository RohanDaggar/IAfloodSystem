# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa

from floodsystem.station import MonitoringStation
from haversine import haversine, unit
def stations_by_distance(stations, p):
    for station in stations:
        distance = haversine(station.coord, p)
    station_and_distance = []
    station_and_distance.append([station.name, station.town, distance])
    return sorted_by_key(station_and_distance, 2)