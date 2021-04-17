from Heap import MaxHeap
import Heapsort

# Program to test the heap class.
h = MaxHeap()
input_list = [25, 44, 55, 99, 30, 37, 15, 10, 2, 4]
for item in input_list:
    h.insert(item)
    print('   --> array: %s\n' % h.heap_array)
print(h)
h = MaxHeap(input_list)
print(h)

numbers = [82, 36, 49, 82, 34, 75, 18, 9, 23]
#numbers = [6, 5, 4, 3, 2, 1]
print("UNSORTED:", numbers)

Heapsort.heap_sort(numbers)
print("SORTED:  ", numbers)
