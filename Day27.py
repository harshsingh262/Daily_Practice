import concurrent.futures
def cube(num):
    print(f"Cube: {num*num*num}")
def square(num):
    print(f"Square: {num*num}")
pool = concurrent.futures.ProcessPoolExecutor(max_workers=None)
pool.submit(cube(10))
pool.submit(square(10))
pool.shutdown(wait=True)
print("Done")