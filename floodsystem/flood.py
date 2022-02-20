from station import check_stations_input
from stationdata import update_water_levels

def stations_level_over_threshold(stations, tol):
    check_stations_input(stations)
    assert type(tol) is int or type(tol) is float
    
    update_water_levels(stations)
    
    rlist = [] #(station, relative water level) for stations above the tolerance
    for station in stations:
        if station.relative_water_level() > tol:
            rlist.append(station, station.relative_water_level())
        
    return rlist