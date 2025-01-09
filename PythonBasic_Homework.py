### Homework Description ###

# create list of 100 random numbers from 0 to 1000
# sort list from min to max (without using sort())
# calculate average for even and odd numbers
# print both average result in console 
# Each line of code should be commented with description.

# import function that generate pseudo random whole numbers
from random import randint

# declare empty list
l = []

# run loop from 0 to 99
for i in range(100):
    # fill our list with random number from 0 to 1000
    l.append(randint(0, 1000))


# function that implements quick sort
def quick_sort(arr):
    # Base case for recursion: if it has 1 or 0 elements - it is sorted
    if len(arr) <= 1:
        return arr

    # choose some random element
    pivot = arr[0]

    # divide out list on two groups
    left = [x for x in arr[1:] if x < pivot]  # lower than pivot
    right = [x for x in arr[1:] if x >= pivot]  # higher or equal than pivot

    # Run recursion to sort left and right part
    sorted_left = quick_sort(left)
    sorted_right = quick_sort(right)

    # combine our data
    return sorted_left + [pivot] + sorted_right


# print raw and sorted list
#print(l)
#print(quick_sort(l))

### calculate average for even and odd numbers
# declare variables for future calculation
even_count = 0
even_sum = 0

odd_count = 0
odd_sum = 0

# run cycle to iterate over the list
for i in range(len(l)):
    if l[i] % 2 == 0:
        even_count += 1
        even_sum += l[i]
    else:
        odd_count += 1
        odd_sum += l[i]

even_avg = even_sum / even_count
odd_avg = odd_sum / odd_count

print(f"Even average is {even_avg}")
print(f"Odd average is {odd_avg}")
