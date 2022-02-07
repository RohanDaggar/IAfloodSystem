from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    a = stations_by_distance(stations, (52.2053,0.1218))
    b = []
    for i in range(len(a)):
        b.append([a[i][0].name, a[i][0].town, a[i][1]])
    print(b[:10])
    print(b[-10:])

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()