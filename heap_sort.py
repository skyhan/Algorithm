# use list to store heap, start from index 1
heap_size = 10

# 堆的根的左右子树都是最大堆，把根节点下沉
def max_heapify(heap_list, i):
    l = left(i)
    r = right(i)
    # get the largest one of root, left, right
    largest = i
    if heap_list[l] > heap_list[i] and l <= heap_size:
        largest = l
    if heap_list[r] > heap_list[i] and r <= heap_size:
        largest = r
    if largest != i:
        swap(heap_list, i, largest)
        max_heapify(heap_list, largest)

# build max heap, i is root index
# heap_size/2+1 to heap_size: leaf node
# i to heap_size/2: non leaf node
def build_max_heap(heap_list, i):
    for j in range(heap_size/2, 1, -1):
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
    2*i+1

# get the father
def father(i):
    return i/2