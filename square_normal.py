import random
import time


def sum_of_squares(numbers):
    return sum(x * x for x in numbers)


list_of_numbers = [
    random.sample(range(1, 101), random.randint(1, 100)) for _ in range(1_000_000)
]

start_time = time.time()

result = [sum_of_squares(numbers) for numbers in list_of_numbers]

end_time = time.time()

print(f"Sequential processing time: {end_time - start_time} seconds")
