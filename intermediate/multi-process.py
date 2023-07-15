from multiprocessing import Process
import os
import time

# dummy process
def sqr_num():
    for i in range(100):
        i * i
        time.sleep(0.1)

process = []
num_process = os.cpu_count()

# create processe

for i in range(num_process):
    p = Process(target=sqr_num)
    process.append(p)

#start
for p in process:
    p.start()

# join, wait for all processes to end
for p in process:
    p.join()

print("end main")
