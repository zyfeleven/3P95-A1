import random
import sys


# quicksort algorithm
def quicksort(arr):
    # if the list is empty, then return
    if len(arr) == 0:
        return arr
    # set the pivot
    pivot = arr[0]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)


# generate a random array
def arrGenerator(length):
    # we can set the range of values
    return [random.randint(-sys.maxsize - 1, sys.maxsize) for _ in range(length)]


# test the algorithm using random arrays
def randomTest():
    # count the number of tests
    count = 1
    # keep looping until finding a bug or achieve an exact number of cases
    while True:
        # if preset count is reached, stop the looping
        if count == 10000:
            return
        # generate a random array with preset length
        arrTemp = arrGenerator(random.randint(1, 10000))
        print(f"test{count}: array length is {len(arrTemp)}")
        try:
            result = quicksort(arrTemp)
            # test whether the result is correct
            # if the length is different, then the result is not correct
            if len(result) != len(arrTemp):
                print("catch an error:")
                print("input array: ")
                print(arrTemp)
                print("output array: ")
                print(result)
                return
            # test whether the elements in the result are increasing
            for i in range(0, len(result) - 2):
                if result[i] > result[i + 1]:
                    print("catch an error:")
                    print("input array: ")
                    print(arrTemp)
                    print("output array: ")
                    print(result)
                    return
        except Exception as e:
            print(f"There is an error: {e}")
            print(f"input array: {arrTemp}")
            return
        count += 1

# run the random test
randomTest()
