import time

def summation(array):
  a = 0
  for i in array:
    a = a + i
    a
    return a
# runtime for the 1st array n = 10
start = time.time()
summation([85,49,11,33,94,30,20,25,33])
print("Execution time for 1st array:{}".format(time.time() - start))
#runtime for the 2nd array n = 25
start= time.time()
summation([92,14,67,42,77,65,88,27,84,94,35,35,70,89,80,35,55,74,32,25,6,17,25,7,72,16])
print("Execution time for 2nd array:{}".format(time.time() - start))
