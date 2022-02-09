from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

def run():
    centre = (52.2053, 0.1218)
    stations = build_station_list()
    r = 10
    station_names_within_distance = sorted([station.name for station in stations_within_radius(stations,centre,r)])
    print(station_names_within_distance)

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()