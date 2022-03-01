from floodsystem.datafetcher import fetch_latest_water_level_data, fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level
import datetime
import numpy as np
import matplotlib.pyplot as plt
from datetime import timedelta  


def run():
    stations = build_station_list()
    update_water_levels(stations)
    station = stations_highest_rel_level(stations, 5)

    for s in range(len(station)):
        dates, levels = fetch_measure_levels(station[s].measure_id, dt=datetime.timedelta(days=10))
        plot_water_levels(s,dates,levels)
        plt.title(station[s].name)
       
if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()    