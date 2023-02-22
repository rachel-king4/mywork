# lab_number_queue.py
# this program puts 10 random numbers into a queue (list)
# and outputs all values in queue
# then take the numbers form queue one at a time
# and prints it and number still in the queue
# Author: Rachel King

import random
queue = []
number_of_numbers = 10
range_to = 100

for n in range(0, number_of_numbers):
    queue.append(random.randint(0,range_to))

print(f"queue is {queue}")

while len(queue) != 0:

    current_number = queue.pop(0)
    print (f"current number is {current_number} and the queue is {queue} ")

print("the queue is now empty")
