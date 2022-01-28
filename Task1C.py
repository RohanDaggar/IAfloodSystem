from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list
    
centre = (52.2053, 0.1218)
stations = build_station_list()
r = 10
less_than_10 = stations_within_radius(stations, centre, r)

print(less_than_10)