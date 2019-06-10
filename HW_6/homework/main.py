'''
This is the official implementation for all the problems for every assignment given in question
'''

import counting_sort as cs
import bucket_sort as bs
import sort_words as sw
import holerith_sorting as hs

# For problem 1.a
print("Couting sort", cs.counting_sort([9, 1, 6, 7, 6, 2, 1]))

#For problem 1.b
print("Bucket sort", bs.bucket_sort([0.9, 0.1, 0.6, 0.7, 0.6, 0.3, 0.1]))

# For problem 1.d
print("Word sort", sw.word_sort(["word", "category", "cat", "new", "news", "world", "bear", "at", "work", "time"]))

# For problem 2.a
arr =  [6, 7, 4, 333, 22, 23, 21, 444, 123, 1233, 1123, 1, 0, 12, 440, 11, 1233]
sorter = hs.Sort(arr)
print("Holerith sort", sorter.radix_sort())
