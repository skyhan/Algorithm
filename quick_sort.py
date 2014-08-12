from datetime import datetime

def quick_sort(list, left, right):
    if left < right:
        i = left
        j = right
        base_number = list[i]
        
        while(i < j):
            while(i < j):
                if list[j] < base_number:
                    list[i] = list[j]
                    i += 1
                    break
                else:
                    j -= 1
            while(i < j):
                if list[i] > base_number:
                    list[j] = list[i]
                    j -= 1
                    break
                else:
                    i += 1
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