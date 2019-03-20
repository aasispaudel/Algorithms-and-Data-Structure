
# coding: utf-8

# In[96]:


import matplotlib.pyplot as plt
import numpy as np
import quick_sort
from time import time
import random


# In[97]:


arr = [1, 1, 4, 3, 2, 7, 6, 5]                                                                                                            
sort1 = quick_sort.Quicksort(arr)                                                                                                                    
sort2 = quick_sort.Quicksort(arr, partition='HOARE')                                                                                                 
sort3 = quick_sort.Quicksort(arr, mid_pivot=True)                                                                                                    
sort4 = quick_sort.Quicksort(arr, mid_pivot=True, partition='HOARE')                                                                                 

lomuto = []
hoare= []
lomuto_v = []
hoare_v = []

X = []

print('Generatin data')

for i in range(int(10e4)):
    arr = [random.randrange(100000) for _ in range(1000)] 
    
    start = time()
    sort1.quick_sort()
    
    check_pt1 = time()
    sort2.quick_sort()
    
    check_pt2 = time()
    sort3.quick_sort()

    check_pt3 = time()
    sort4.quick_sort()
    
    end = time()

    X.append(1000)
    lomuto.append(check_pt1-start)
    hoare.append(check_pt2-check_pt1)
    lomuto_v.append(check_pt3-check_pt2)
    hoare_v.append(end-check_pt3)


# In[99]:


def avg(x):
    return sum(x)/len(x)

# In[100]:


def avg(x):
    return sum(x)/len(x)

print(f'Lomoto:{avg(lomuto)} Hoare:{avg(hoare)}'
f'Lomoto with best pivot: {avg(lomuto_v)}'
f'Hoare with best pivot: {avg(hoare_v)}'
)

