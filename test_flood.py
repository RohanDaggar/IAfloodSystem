from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
stations = build_station_list()
update_water_levels(stations)

def test_stations_level_over_threshold():
    s_id1 = "test-s-id"
    m_id1 = "test-m-id"
    label1 = "some station"
    coord1 = (-2.0, 4.0)
    trange1 = (-2.3, 2.384)
    river1 = "River X"
    town1 = "My Town"
    latest_level1 = 6
    s1 = MonitoringStation(s_id1, m_id1, label1, coord1, trange1, river1, town1)
    s1.latest_level = latest_level1
    
    s_id2 = "test-s-id"
    m_id2 = "test-m-id"
    label2 = "some station"
    coord2 = (-2.0, 4.0)
    trange2 = (-2.3, 2.384)
    river2 = "River X"
    town2 = "My Town"
    latest_level2 = 0
    s2 = MonitoringStation(s_id2, m_id2, label2, coord2, trange2, river2, town2)
    s2.latest_level = latest_level2
    
    stations = [s1, s2]
    assert len(stations_level_over_threshold(stations, 100)) == 0
    assert len(stations_level_over_threshold(stations, -100)) == 2
    assert len(stations_level_over_threshold(stations, 0.8)) == 1
    test = stations_level_over_threshold(stations, 0)
    for item in test:
        assert type(item) is tuple
        assert len(item) == 2
        assert type(item[0]) is MonitoringStation
        assert type(item[1]) is float
        
def test_stations_highest_rel_level():
    station_list = stations_highest_rel_level(stations, 10)
    assert len(station_list) == 10
    for station in station_list:
        assert type(station) is MonitoringStation