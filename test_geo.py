"""Unit test for the geo module"""
import pytest
from floodsystem.stationdata import build_station_list
stations = build_station_list()

from floodsystem.geo import *

def test_stations_by_distance():
    result = stations_by_distance(stations,(0,0))
    
    #this first tests that all the stations are very far from (0,0), which it should be
    for item in result:
        assert item[1] > 5000
    
    #these lines makes sure an ValueError is raised for the wrong input
    with pytest.raises(Exception) as e_info:
        x = stations_by_distance(stations,(0,0,"how did this get in here"))
    with pytest.raises(Exception) as e_info:
        x = stations_by_distance(stations,(0,"how did this get in here"))
    
def test_stations_within_radius():
    #checks that no stations are around (0,0)
    result = stations_within_radius(stations,(0,0),5)
    assert type(result) is list
    assert len(result) == 0
    
    #checks that some stations are within cam
    assert len(stations_within_radius(stations, (52.2053, 0.1218), 10)) > 0

def test_rivers_with_stations():
    x = rivers_with_station(stations)

def test_stations_by_river():
    x = stations_by_river(stations)

def test_rivers_by_station_number():
    #runs through known answers
    #! need to re do this
    """assert (len(rivers_by_station_number(stations,1))) == 1
    assert (len(rivers_by_station_number(stations,2))) == 2
    assert (len(rivers_by_station_number(stations,8))) == 8
    assert (len(rivers_by_station_number(stations,9))) == 10
    assert (len(rivers_by_station_number(stations,10))) == 10
    assert (len(rivers_by_station_number(stations,949))) == 950
    assert (len(rivers_by_station_number(stations,950))) == 950
    assert (len(rivers_by_station_number(stations,951))) == 950
    assert (len(rivers_by_station_number(stations,10000))) == 950"""
