#coding:utf-8
# use list to store heap, start from index 1
from datetime import datetime
heap_size = 0

def heap_sort(heap_list):
    global heap_size
    build_max_heap(heap_list)
    for i in range(0, heap_size):
        swap(heap_list, 1, heap_size)
        heap_size -= 1

# 堆的根的左右子树都是最大堆，把根节点下沉
def max_heapify(heap_list, i):
    global heap_size
    l = left(i)
    r = right(i)
    
    # get the largest one of root, left, right
    largest = i
    if l <= heap_size and heap_list[l] > heap_list[i]:
        largest = l
    if r <= heap_size and heap_list[r] > heap_list[i]:
        largest = r
    if largest != i:
        swap(heap_list, i, largest)
        max_heapify(heap_list, largest)

# build max heap, i is root index
# heap_size/2+1 to heap_size: leaf node
# i to heap_size/2: non leaf node
def build_max_heap(heap_list):
    global heap_size
    for j in range(heap_size/2, 0, -1):
        max_heapify(heap_list, j)

def swap(list, i, j):
    tmp = list[i]
    list[i] = list[j]
    list[j] = tmp

# get the left child
def left(i):
    return 2*i

# get the right child
def right(i):
    return 2*i+1

# get the father
def father(i):
    return i/2

def generate_list():
    global heap_size
    import random
    list = []
    list.append(-1) # do not use list[0], start to store from index 1
    for i in range(0, heap_size):
        list.append(random.randint(0,10000))
    return list

if __name__ == '__main__':
    print 'heap sort'
    heap_size = 20
    list = generate_list()
    print list
    start_time = datetime.now()
    heap_sort(list)
    end_time = datetime.now()
    print list
    print end_time - start_time