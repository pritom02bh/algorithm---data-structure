import time

# start time
start = time.time()

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

print(fact(55))

# end time
end = time.time()

# total time taken
print(f"Runtime of the function is {end - start}")
