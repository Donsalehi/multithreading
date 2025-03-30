import threading

storage = [0] * 100

def writing(p, num):
    end = p * 20
    first = end - 20
    for i in range(first, end):
        storage[i] = num

def reading(p):
    end = p * 20
    first = end - 20
    for i in range(first, end):
        print(storage[i])

print("Start!")

t1 = threading.Thread(target=writing, args=(1, 1))
t2 = threading.Thread(target=writing, args=(2, 2))
t3 = threading.Thread(target=writing, args=(3, 3))
t4 = threading.Thread(target=writing, args=(4, 4))
t5 = threading.Thread(target=writing, args=(5, 5))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()

t1 = threading.Thread(target=reading, args=(1, ))
t2 = threading.Thread(target=reading, args=(2, ))
t3 = threading.Thread(target=reading, args=(3, ))
t4 = threading.Thread(target=reading, args=(4, ))
t5 = threading.Thread(target=reading, args=(5, ))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()

print("Done!")