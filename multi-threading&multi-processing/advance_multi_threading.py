from concurrent.futures import ThreadPoolExecutor
import time

def print_numbers(numbers):
    time.sleep(2)
    return f'Number: {numbers}'

numbers=[1,2,3,4,5,6,7,8,9,10]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_numbers,numbers)

for result in results:
    print(result) 