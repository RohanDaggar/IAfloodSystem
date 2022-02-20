from floodsystem.station import check_stations_input
from floodsystem.utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    #assumes that station objects have updates water levels already
    check_stations_input(stations)
    assert type(tol) is int or type(tol) is float
    
    rlist = [] #(station, relative water level) for stations above the tolerance
    for station in stations:
        try:
            if station.relative_water_level() > tol:
                rlist.append((station, station.relative_water_level()))
        except TypeError:
            pass
    
    return sorted_by_key(rlist, 1, reverse=True)
