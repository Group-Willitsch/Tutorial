import numpy as np
import time

print("Hello my friend how are you ?")

length = 1000000000
to_add = 2**4

my_list = []
my_nparray = np.zeros((length))

start_time = time.time()
for i in range(length):
    my_nparray[i] = to_add
end_time = time.time()

print(end_time - start_time)

start_time = time.time()
for i in range(length):
    my_list.append(to_add)
end_time = time.time()

print(end_time - start_time)

start_time = time.time()
my_complist = [to_add for i in range(length)]
end_time = time.time()

print(end_time - start_time)

# print(my_list)
# print(my_nparray)
# print(my_complist)