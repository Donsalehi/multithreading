import threading


storage = [0] * 40

flag = [False, False]
turn = 0

def writing(p, num, thread_id):
    global turn
    flag[thread_id] = True

    while flag[1 - thread_id]:
        if turn != thread_id:
            flag[thread_id] = False
            while turn != thread_id:
                pass
            flag[thread_id] = True

    #critical section
    end = p * 20
    first = end - 20
    for i in range(first, end):
        storage[i] = num

    turn = 1 - thread_id
    flag[thread_id] = False

def reading(p, thread_id):
    global turn
    flag[thread_id] = True

    while flag[1 - thread_id]:
        if turn != thread_id:
            flag[thread_id] = False
            while turn != thread_id:
                pass
            flag[thread_id] = True
    
    #critical section
    end = p * 20
    first = end - 20
    for i in range(first, end):
        print(storage[i])
    
    turn = 1 - thread_id
    flag[thread_id] = False


print("Start!")

t1 = threading.Thread(target=writing, args=(1, 1, 0))
t2 = threading.Thread(target=writing, args=(2, 2, 1))

t1.start()
t2.start()

t1.join()
t2.join()

t1 = threading.Thread(target=reading, args=(1, 0))
t2 = threading.Thread(target=reading, args=(2, 1))

t1.start()
t2.start()

t1.join()
t2.join()

print("Done!")