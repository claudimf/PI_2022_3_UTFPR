# docker-compose run --rm app python3 ler.py
import shapefile
import pandas as pd

sf = shapefile.Reader("estados.shp")
print(sf)
print(sf.fields)