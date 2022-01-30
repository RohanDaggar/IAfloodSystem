from floodsystem.stationdata import build_station_list
stations = build_station_list()

from floodsystem.geo import *

def test_rivers_by_station_number():
    assert (len(rivers_by_station_number(stations,1))) == 1
    assert (len(rivers_by_station_number(stations,2))) == 2
    assert (len(rivers_by_station_number(stations,8))) == 8
    assert (len(rivers_by_station_number(stations,9))) == 10
    assert (len(rivers_by_station_number(stations,10))) == 10
    
def test_stations_within_radius():
    result = stations_within_radius(stations,(0,0),5)
    assert type(result) is list
    assert len(result) == 0