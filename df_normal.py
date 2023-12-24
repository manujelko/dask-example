import pandas as pd
import numpy as np
from time import time


df = pd.DataFrame(
    np.random.randint(0, 100, size=(10_000_000, 5)),
    columns=["col1", "col2", "col3", "col4", "col5"],
)
df["group"] = np.random.randint(0, 100, size=10_000_000)

start = time()
result_pandas = df.groupby("group").sum()
end = time()

print(f"Pandas processing time: {end - start} seconds")
