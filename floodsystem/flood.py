from floodsystem.station import check_stations_input
from floodsystem.utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    """a function that returns a list of tuples, where each tuple holds (i) a station (object) at which the latest relative water
    level is over tol and (ii) the relative water level at the station. The returned list should be sorted by the relative level in
    descending order.

    Args:
        stations (list): list of monitoring station objects with live water levels attached
        tol (int/float): the tolerance in which to return

    Returns:
        list: list of (station, relative water level) tuples
    """
    #assumes that station objects have updates water levels already
    check_stations_input(stations)
    assert type(tol) is int or type(tol) is float
    
    rlist = [] #(station, relative water level) for stations above the tolerance
    for station in stations:
        try:
            if station.relative_water_level() > tol:
                if station.relative_water_level() > 500:
                    break
                rlist.append((station, station.relative_water_level()))
        except TypeError:
            pass
    
    return sorted_by_key(rlist, 1, reverse=True)

def stations_highest_rel_level(stations, N):
    
    check_stations_input(stations)
    assert type(N) is int
    
    sorted_list = stations_level_over_threshold(stations, -100) #The -100 returns all stations, sorted
    just_objects_list = [item[0] for item in sorted_list]
    
    return just_objects_list[:N]
    
    
    