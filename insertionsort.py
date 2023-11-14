unsorted_list = [1,2,4,3,5]
def insertion_sort(unsorted):
    sorted = []
    for i in range(0,len(unsorted)):
        print(sorted)
        value = unsorted[i]
        if i == 0:
            sorted.append(value)
        else:
            if value >= sorted[-1]:
                sorted.append(value)
            else:
                sorted.append(sorted[-1])
                for j in range(1, i+1):
                    compare_i = i-j
                    print('compare_i is', compare_i)
                    compare_val = sorted[compare_i]
                    print('value is', value)
                    print('compare val is ', compare_val)
                    if value < compare_val:
                        print('sorted is', sorted)
                        working_value_1 = sorted[compare_i-1]
                        print ('working value 1 is', working_value_1)
                        working_value_2 = sorted[compare_i]
                        print ('working value 2 is', working_value_2)
                        sorted[compare_i] = working_value_1
                        sorted[compare_i-1] = working_value_2
                    if value >= compare_val:
                        sorted[compare_i] = value
                        break
    return(sorted)
print (unsorted_list)
print (insertion_sort(unsorted_list))
