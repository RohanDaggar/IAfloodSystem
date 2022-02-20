from floodsystem.station import MonitoringStation

def test_stations_level_over_threshold():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 2.384)
    river = "River X"
    town = "My Town"
    latest_level = 6
    s1 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s1.latest_level = latest_level
    
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 2.384)
    river = "River X"
    town = "My Town"
    latest_level = 0
    s2 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    