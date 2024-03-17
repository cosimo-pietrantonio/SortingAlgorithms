import sorting
import time

if __name__=='__main__':
    
    x=[10,2,1,2,14,5,6,11]
    
    print('Bubble sort algorithm:\n')
    print(f'Starting array: {x}\n')
    
    start_time = time.time()
    bubble_x = sorting.bubblesort(x.copy())
    
    print(f'Sorted array: {bubble_x}\n')
    print("--- %s seconds ---" % (time.time() - start_time))

    print('\n\n Merge sort algorithm:\n')
    print(f'Starting array: {x}\n')
    
    start_time = time.time()
    bubble_x = sorting.mergesort(x.copy())
    
    print(f'Sorted array: {bubble_x}\n')
    print("--- %s seconds ---" % (time.time() - start_time))
    
    