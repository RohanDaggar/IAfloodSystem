from floodsystem.stationdata import build_station_list
stations = build_station_list()

from floodsystem.geo import rivers_by_station_number
print(rivers_by_station_number(stations,9))