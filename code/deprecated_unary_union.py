from shapely import Polygon
import geopandas as gpd

p1 = Polygon([[1, 2], [3, 2], [3, 4], [1, 4]])
p2 = Polygon([[2, 3], [4, 3], [4, 5], [2, 5]])

gpd.GeoDataFrame(geometry=[p1, p2]).unary_union
