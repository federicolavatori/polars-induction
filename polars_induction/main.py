import polars as pl

# to enrich the examples in this quickstart with dates
from datetime import datetime, timedelta
# to generate data for the examples
import numpy as np

# with a tuple
series = pl.Series("a", [1, 2, 3, 4, 5])

print(series)


dataframe = pl.DataFrame({"integer": [1, 2, 3],
                          "date": [
                              (datetime(2022, 1, 1)),
                              (datetime(2022, 1, 2)),
                              (datetime(2022, 1, 3))
                          ],
                          "float":[4.0, 5.0, 6.0]})

print(dataframe)

dataframe.write_csv('output.csv')

df_csv_with_dates = pl.read_csv('output.csv', try_parse_dates=True)

print(df_csv_with_dates)





