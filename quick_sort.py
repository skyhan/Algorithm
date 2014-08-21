from datetime import datetime
# choose list[right] as primary compare number
# part the list into two parts
# left to i: < list[right]
# i+1 to right: > list[right]
def quick_sort(list, left, right):
    if left < right:
        i = left -1
        for j in range(left, right):
            if list[j] < list[right]:
                i += 1
                swap(list, i, j)
        # swap list[right] to the middle, i is the middle index
        i += 1
        swap(list, i, right)
        quick_sort(list, left, i-1)
        quick_sort(list, i + 1, right)

def swap(list, i, j):
    tmp = list[i]
    list[i] = list[j]
    list[j] = tmp

def generate_list():
    import random
    list = []
    for i in range(0, 20):
        list.append(random.randint(0,10000))
    return list

if __name__ == '__main__':
    print 'quick sort'
    list = generate_list()
    print list
    start_time = datetime.now()
    quick_sort(list, 0, len(list)-1)
    end_time = datetime.now()
    print list
    print end_time - start_time