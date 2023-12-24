import random
import time

from dask import compute, delayed  # type: ignore


def sum_of_squares(numbers: list[int]):
    return sum(x * x for x in numbers)


list_of_numbers = [
    random.sample(range(1, 101), random.randint(1, 100)) for _ in range(1_000_000)
]

tasks = [delayed(sum_of_squares)(numbers) for numbers in list_of_numbers]

start_time = time.time()
results = compute(*tasks)
end_time = time.time()
print(f"Dask processing time: {end_time - start_time} seconds")
