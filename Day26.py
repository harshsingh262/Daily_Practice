import multiprocessing
def printcube(num):
    print(f"Cube: {num*num*num}")
def printsquare(num):
    print(f"Square: {num*num}")
t1 = multiprocessing.Process(target = printcube, args = [10])
t2 = multiprocessing.Process(target = printsquare, args = [10])
t1.start()
t2.start()
t1.join()
t2.join()
print("Done!")