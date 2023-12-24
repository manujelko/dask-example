from time import time

import dask.dataframe as dd
import numpy as np
import pandas as pd

n_rows = 10_000_000
n_columns = 5

df = pd.DataFrame(
    np.random.randint(0, 100, size=(n_rows, n_columns)),
    columns=[f"col{i}" for i in range(n_columns)],
)

df["group"] = np.random.randint(0, 100, size=n_rows)

ddf = dd.from_pandas(df, npartitions=10)  # type: ignore

start = time()

result = ddf.groupby("group").sum().compute()

end = time()

print(f"Dask processing time: {end - start} seconds")
