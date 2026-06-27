from . import main, areas, stations, areas_and_stations, info, hubs

PAGES = (
    [main.PAGE] +
    hubs.PAGES +
    areas.PAGES +
    stations.PAGES +
    areas_and_stations.PAGES +
    info.PAGES
)
