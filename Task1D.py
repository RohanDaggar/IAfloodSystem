from floodsystem.geo import rivers_with_station, stations_by_river
from floodsystem.stationdata import build_station_list

def run():
    b = build_station_list()
    print("{} stations. First 10 - " .format(len(rivers_with_station(b))),rivers_with_station(b)[:10])

    rivers_dict = stations_by_river(b)
    print("River Aire:")
    print(rivers_dict["River Aire"])
    print("River Cam:")
    print(rivers_dict["River Cam"])
    print("River Thames:")
    print(rivers_dict["River Thames"])