from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

def run():
    centre = (52.2053, 0.1218)
    stations = build_station_list()
    r = 10
    less_than_10 = stations_within_radius(stations, centre, r)

    print(less_than_10)

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()