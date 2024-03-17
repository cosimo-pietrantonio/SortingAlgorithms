def bubblesort(array: list[int])->list[int]:
    for i in range(len(array)-1):
        for j in range(i,len(array)):
            if array[i] > array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    return array


def mergesort(array: list[int])->list[int]:
    
    if len(array) > 1:
        # Splitting
        mid_array = len(array)//2
        left_array = array[:mid_array]
        right_array = array[mid_array:]

        # Recursion until each array contains just one element
        mergesort(left_array)
        mergesort(right_array)

        # Sorting step
        lidx = 0
        ridx = 0
        sorted_idx = 0

        while lidx < len(left_array) and ridx < len(right_array):
            if left_array[lidx] < right_array[ridx]:

                array[sorted_idx] = left_array[lidx]
                lidx += 1    
            else:
                
                array[sorted_idx] = right_array[ridx]
                ridx += 1
            
            sorted_idx += 1
        
        # Append the remaining values
        while lidx < len(left_array):
            array[sorted_idx] = left_array[lidx]
            sorted_idx += 1
            lidx += 1
        
        while ridx < len(right_array):
            array[sorted_idx] = right_array[ridx]
            sorted_idx += 1
            ridx += 1

        return array