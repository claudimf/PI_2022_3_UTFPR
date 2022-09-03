# docker-compose run --rm app python3 test1.py
import pandas as pd
from pytrends.request import TrendReq


def related_topics_rising(trend):
    pytrends = TrendReq(hl='pt-BR', tz=360)
    pytrends.build_payload(kw_list=[trend], timeframe='now 1-d', geo='BR', gprop='')
    related_rising = pytrends.related_topics()
    try:
        rising = pd.DataFrame.from_dict(related_rising[trend]['rising'])
        return rising
    except Exception as e:
        rising = None
        raise e

print(related_topics_rising('Tesla'))