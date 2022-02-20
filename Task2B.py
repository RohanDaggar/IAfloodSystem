from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():
    stations = build_station_list()
    update_water_levels(stations)
    
    for item in stations_level_over_threshold(stations, 0.8):
        station, level = item
        print(station.name, level)

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
