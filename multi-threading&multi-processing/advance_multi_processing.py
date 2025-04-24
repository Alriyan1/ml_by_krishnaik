from concurrent.futures import ProcessPoolExecutor
import time

def print_number(number):
    time.sleep(2)
    return f'Number: {number*number}'

number=[1,3,4,2,5]
if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(print_number, number)

    for result in results:
        print(result)