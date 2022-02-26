import matplotlib.pyplot as plt
from floodsystem.stationdata import build_station_list

def plot_water_levels(station, dates, levels):
    
    plt.plot(dates, levels)
    
    plt.title('stations.name')
    plt.xlabel('Date')
    plt.ylabel('Water Level (m)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()