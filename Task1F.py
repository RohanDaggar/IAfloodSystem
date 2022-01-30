from floodsystem.stationdata import build_station_list
from floodsystem.station import *

def run():
    stations = build_station_list()
    inconsistent_list = inconsistent_typical_range_stations(stations)

    #this block turns the list of stations into the list of just the names of the stations
    inconsistent_list_names=[]
    for station in inconsistent_list:
        inconsistent_list_names.append(station.name)
    inconsistent_list_names.sort()

    print(inconsistent_list_names)