from floodsystem.datafetcher import fetch_latest_water_level_data, fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level
import datetime
import numpy as np
from datetime import timedelta  


def run():
    stations = build_station_list()
    update_water_levels(stations)
    station = stations_highest_rel_level(stations, 5)

    #a = []
    #station_name = []
    #c = []
    #b = []
    # Find station
    #station_cam = None
    #for station in stations:
    #    if station.name == station_name:
    #        station_cam = station
    #        break
    #dt = 2
    #b = fetch_measure_levels(station_cam.measure_id, dt=datetime.timedelta(days=dt))
    #dates, levels = [], []
    #dt = 2
    #for i in range(len(station)):
     #   a.append(station[i])
      #  station_name.append(a[i].name)
        #b.append(fetch_measure_levels(a[i].measure_id, dt=datetime.timedelta(days=dt)))
        
    #for k in range(len(a)):
     #   b.append(fetch_measure_levels(a[1].measure_id, dt=datetime.timedelta(days=dt)))
      #  b.append(fetch_measure_levels(a[2].measure_id, dt=datetime.timedelta(days=dt)))
        #c.append(b[k])
        #dates.append(fetch_measure_levels(a[k].measure_id, dt=datetime.timedelta(days=dt))[k][0])
        #levels.append(fetch_measure_levels(a[k].measure_id, dt=datetime.timedelta(days=dt))[k][0])
    
    #station_name = 
    #b = fetch_measure_levels()
    
    #print(a)
    #for date, level in zip(b[0][:], b[:][1]):
    #    print(date,level)
    #print(b)
    #d = np.asarray(b)
    #print(d.flatten()[:,1])
    #plot_water_levels(station, dates, levels)
    for s in station:
        dates, levels = fetch_measure_levels(station[s].measure_id,
                                     dt=datetime.timedelta(days=10))
        plot_water_levels(s,dates,levels)
       
if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()    