import math
import pandas as pd
from shapely.geometry import Point
from geopandas import GeoDataFrame


# returns Great Circle Distance in KM for two points in WGS84 coordinate system
def gcdist(lat1, lon1, lat2, lon2):
    R = 6378.137

    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    lon1 = math.radians(lon1)
    lon2 = math.radians(lon2)

    lat_span = lat1 - lat2
    lon_span = lon1 - lon2

    a = math.sin(lat_span / 2) ** 2
    b = math.cos(lat1)
    c = math.cos(lat2)
    d = math.sin(lon_span / 2) ** 2

    dist = 2 * R * math.asin(math.sqrt(a + b * c * d))

    return dist


# projects coordinate pair from WGS84 coordinate system to different one
def transform(lat, lon, projection):
    df = pd.DataFrame({'Lat': [lat],
                       'Lon': [lon]})

    geometry = [Point(lon, lat)]
    gdf = GeoDataFrame(df, geometry=geometry)

    gdf.set_crs(epsg=4326, inplace=True)

    projected = gdf.to_crs(epsg=projection).geometry[0]
    return projected.x, projected.y
