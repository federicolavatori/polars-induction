import polars as pl

# to enrich the examples in this quickstart with dates
from datetime import datetime, timedelta
# to generate data for the examples
import numpy as np

# with a tuple
series = pl.Series("a", [1, 2, 3, 4, 5])

print(series)


