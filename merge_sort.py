import sys
from datetime import datetime

def merge_sort(list, start, end):
    if start < end:
        middle = (end + start) / 2
        merge_sort(list, start, middle)
        merge_sort(list, middle + 1, end)
        merge_ordered_list(list, start, middle, end)

def merge_ordered_list(list, list1_start, list1_end, list2_end):
    # create two tmp list to store original list
    list1 = list[list1_start:list1_end+1]
    list2 = list[list1_end+1:list2_end+1]
    # add max int to two list
    list1.append(sys.maxint)
    list2.append(sys.maxint)
    
    list1_index = 0
    list2_index = 0
    for i in range(list1_start, list2_end+1):
        if list1[list1_index] < list2[list2_index]:
            list[i] = list1[list1_index]
            list1_index += 1
        else:
            list[i] = list2[list2_index]
            list2_index += 1

def generate_list():
    import random
    list = []
    for i in range(0, 20):
        list.append(random.randint(0,10000))
    return list

if __name__ == '__main__':
    print 'merge sort'
    list = generate_list()
    print list
    start_time = datetime.now()
    merge_sort(list, 0, len(list)-1)
    end_time = datetime.now()
    print list
    print end_time - start_time