from multiprocessing import Process
from time import sleep

def f(r, n):
    for i in range(r):
        print(i,r)
        sleep(1)

p1 = Process(target=f, args=(4,"a"))
p2 = Process(target=f, args=(9,"b"))
p3 = Process(target=f, args=(3,"c"))

p1.start()
p2.start()
p3.start()


