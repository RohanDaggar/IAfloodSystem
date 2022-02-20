# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation, check_coordinate_input
import pytest

def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_check_coordinate_input():
    #checks working coordinates to make sure the test function works
    
    check_coordinate_input((0,0))
    check_coordinate_input((0.5431,0.6431))
    check_coordinate_input((-3252,5123.5325))
    check_coordinate_input((-34,0))
    check_coordinate_input((0.0,-5.2))
    
    #checks invalid coordinates to make sure it returns an exception
    with pytest.raises(Exception) as e_info:
        check_coordinate_input(0)
        check_coordinate_input("Test")
        check_coordinate_input([0,0])
        check_coordinate_input(("Hi",0))
        check_coordinate_input((0,0,0,5))

def test_relative_water_level():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 2.384)
    river = "River X"
    town = "My Town"
    latest_level = 6
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    
    s.latest_level = latest_level
    
    assert s.relative_water_level() == (latest_level-trange[0])/(trange[1]-trange[0])
