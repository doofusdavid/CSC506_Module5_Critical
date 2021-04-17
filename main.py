from Heap import MaxHeap
# Program to test the heap class.
h = MaxHeap()
input_list = [10, 2, 5, 18, 22]
for item in input_list:
    h.insert(item)
    print('   --> array: %s\n' % h.heap_array)
while len(h.heap_array) > 0:
    removed_value = h.remove()
    print('   --> removed %d, array: %s\n' % (removed_value, h.heap_array))
print()
