from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
import matplotlib
from matplotlib.dates import date2num
from floodsystem.datafetcher import fetch_measure_levels
import datetime
from floodsystem.analysis import polyfit


def predicted_relative_water_level(station, prediction):
    return (prediction - station.typical_range[0]) / (station.typical_range[1] - station.typical_range[0])


def run():

    stations = build_station_list()
    update_water_levels(stations)

    station = stations_highest_rel_level(stations, 20)

    target_stations = []

    for s in station:
        dates, levels = fetch_measure_levels(s.measure_id, dt=datetime.timedelta(days=2))
        if len(dates) < 1 or len(levels) < 1:
            continue

        poly, d0 = polyfit(dates, levels, 4)
        time = date2num(dates)
        
        current = max(time - d0)
        prediction = poly(current + 1)

        rise = predicted_relative_water_level(s, prediction) - s.relative_water_level()

        if predicted_relative_water_level(s, prediction) > s.relative_water_level():
            target_stations.append([s.name, rise])
            print("{}:\n\tRelative water level: {}\n\tPredicted relative water level: {}\n\tRise: {}".format(
                s.name, s.relative_water_level(), predicted_relative_water_level(s, prediction), rise))

    target_towns = []

    for i, stations_risk in enumerate(target_stations):
        if stations_risk[0] in [towns for towns, count in target_towns]:
            target_towns[i][1] += stations_risk[1]
        else:
            target_towns.append(stations_risk[:])

    print('List of target towns and the estimated flood risk:')
    print(target_towns)

    #print('-' * 70)
    #print('The towns where the risk of flooding is assessed to be the greatest:')

    ratings = ['low', 'moderate', 'high', 'severe']
    for town, risk in target_towns:
        rating_factor = 0  # low
        if risk > 0.5:
            rating_factor = 1  # moderate
        if risk > 5:
            rating_factor = 2  # high
        if risk > 10:
            rating_factor = 3  # severe
        print('{}:\n\t{}'.format(town, ratings[rating_factor]))
        
if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()
    
    