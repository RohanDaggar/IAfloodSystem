"""This will test this module that is held within floodsystem/geo.py"""
from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list
stations = build_station_list()

result = stations_within_radius(stations,(0,0),5)
assert type(result) is list
assert len(result) == 0