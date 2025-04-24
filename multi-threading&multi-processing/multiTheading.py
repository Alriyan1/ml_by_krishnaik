import threading
import time

def print_number():
    for i in range(5):
        time.sleep(1)
        print(f'Number: {i}')

def print_letter():
    for i in 'abcde':
        time.sleep(1)
        print(f'Letter: {i}')


t=time.time()
t1=threading.Thread(target=print_number)
t2=threading.Thread(target=print_letter)

t1.start()
t2.start()  

t1.join()
t2.join()

fineshed_time=time.time()-t
print(fineshed_time)