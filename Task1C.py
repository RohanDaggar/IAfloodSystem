from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

def run():
    centre = (52.2053, 0.1218)
    stations = build_station_list()
    r = 10
    less_than_10 = stations_within_radius(stations, centre, r)
    c = []
    for i in range(len(less_than_10)):
        c.append([less_than_10[i][0].name])
    c.sort()
    print(c)

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()