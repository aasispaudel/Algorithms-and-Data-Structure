import q_variant as q_
import quick_sort as q
# import data_generation
from random import randrange as rd

arr = [rd(1000) for _ in range(100)]
sort1 = q.Quicksort(arr)
sort2 = q.Quicksort(arr, partition='HOARE')
sort3 = q.Quicksort(arr, mid_pivot=True)
sort4 = q.Quicksort(arr, mid_pivot=True, partition='HOARE')

print('lomuto:', sort1.quick_sort())
print('hoare: ', sort2.quick_sort())
print('lomuto with median_pivot', sort3.quick_sort())
print('hoare with median_pivot', sort4.quick_sort())

sort_ = q_.Quicksort(arr)
print('The variation: ', sort_.quick_sort())
    
import data_generation
