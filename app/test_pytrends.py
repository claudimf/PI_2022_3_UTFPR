# docker-compose run --rm app python3 test_pytrends.py
import pandas as pd
from pytrends.request import TrendReq
pytrend = TrendReq()
pytrend.build_payload(kw_list=['Taylor Swift'])
# Interest by Region
print('\nPesquisando...')
df = pytrend.interest_by_region()
df.head(10)
print(df.head(10))