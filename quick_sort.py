from datetime import datetime

def quick_sort(list, left, right):
    if left < right:
        i = left
        j = right
        base_number = list[i]
        
        while(i < j):
            while(i < j and list[j]>= base_number):
                j -= 1
            if(i < j):
                list[i] = list[j]
                i += 1
            while(i < j and list[i] <= base_number):
                i += 1
            if (i < j):
                list[j] = list[i]
                j -= 1
        list[i] = base_number
        
        
        quick_sort(list, left, i-1)
        quick_sort(list, i + 1, right)

if __name__ == '__main__':
    print 'quick sort'
    list = [4, 3, 5, 2, 7, 1, 9]
    print list
    start_time = datetime.now()
    quick_sort(list, 0, len(list)-1)
    end_time = datetime.now()
    print list
    print end_time - start_time