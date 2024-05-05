# Alex Giang
# Professor Abolghasemi
# CIS 502
# 11 March 2024

# Week 12, Exercise

# This file is intended to demonstrate beginning knowledge in implementing
# multithreading to run different functions at once.
import threading
import os
import time

def print_square(num):
    time.sleep(0.18)
    print(num ** 2)


def print_cube(num):
    time.sleep(0.19)
    print(num ** 3)


def task1():
    print("task1 | Process ID:", os.getpid())
    print("task1 | Thread Name:", threading.current_thread().name)
    print("Time to sleep: 400ms")
    time.sleep(0.01)
    time.sleep(0.39)
    print("Done sleeping... printing square of 5 in 180ms")
    print_square(5)


def task2():
    print("task2 | Process ID:", os.getpid())
    print("task2 | Thread Name:", threading.current_thread().name)
    print("Time to sleep: 700ms")
    time.sleep(0.01)
    time.sleep(0.69)
    print("Done sleeping... printing cube of 5 in 190ms")
    print_cube(5)


def mytimer():
    print("mytimer | Process ID:", os.getpid())
    print("mytimer | Thread Name:", threading.current_thread().name)
    for i in range(0,2000,100):
        print('\t', i, 'ms into execution...')
        time.sleep(0.1)


if __name__ == "__main__":
    print("__main__ | Process ID:", os.getpid())
    print("__main__ | Thread Name:", threading.current_thread().name)
    print("Main sleeps for an addt'l 300ms")

    print("Iteration 1: Targetting task1 and task2")

    t1 = threading.Thread(target=task1, name='t1')
    t2 = threading.Thread(target=task2, name='t2')
    ttime = threading.Thread(target=mytimer, name='ttime')

    t1.start()
    t2.start()
    ttime.start()

    t1.join()
    t2.join()
    ttime.join()

    print("All other threads done...addt'l sleeping")
    time.sleep(0.3)

    print("Done with iteration 1!\n\n")

    print("Iteration 2: Targetting print_square and print_cube with num=7")
    print("Note: only short sleep statements in the print functions!")
    print("Main sleeps for an addt'l 300ms")

    t1 = threading.Thread(target=print_square, name='t1', args=(7,))
    t2 = threading.Thread(target=print_cube, name='t2', args=(7,))
    ttime = threading.Thread(target=mytimer, name='ttime')

    t1.start()
    t2.start()
    ttime.start()

    t1.join()
    t2.join()
    ttime.join()

    print("All other threads done...addt'l sleeping")
    time.sleep(0.3)

    print("Done with iteration 2!\n\n")

    print("Iteration 3: First iteration but concurrently (no joins)")
    print("Main sleeps for 1,500ms")

    t1 = threading.Thread(target=task1, name='t1')
    t2 = threading.Thread(target=task2, name='t2')
    ttime = threading.Thread(target=mytimer, name='ttime')

    t1.start()
    t2.start()
    ttime.start()

    # t1.join()
    # t2.join()
    # ttime.join()
    time.sleep(1.5)

    print("Done with iteration 3!")
    time.sleep(1)
    print("t1 alive? : ", t1.is_alive())
    print("t2 alive? : ", t2.is_alive())
    print("ttime alive? : ", ttime.is_alive())
    print("\nThat means tasks are done!")


