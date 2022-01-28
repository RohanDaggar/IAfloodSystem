from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list

b = build_station_list()
print("{} stations. First 10 - " .format(len(rivers_with_station(b))),rivers_with_station(b)[:10])
print(stations_by_river(b))