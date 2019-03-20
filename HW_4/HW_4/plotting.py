
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt

import real_heapsort as heap_sort


# In[7]:


X_real = []
Y_real = []
X_variant = []
Y_variant = []

from time import time

for i in range(100, int(10e4), 500):
    X_real.append(i)
    X_variant.append(i)
    real_heap = heap_sort.Heapsort(list(range(i)))
    variant_heap = heap_sort.Heapsort(list(range(i)))
    
    start = time()
    real_heap.heap_sort()
    Y_real.append(time()-start)
    
    chect_pt1 = time()
    variant_heap = variant_heap.heap_sort(variant=True)
    Y_variant.append(time()-start)
    
X_real, Y_real, X_variant, Y_variant


# In[16]:


plt.figure()
ax = plt.subplot(111)

# For large values of n
ax.plot(X_real, Y_real, 'm', label='Real heapify')
ax.plot(X_variant, Y_variant, 'y', label='Variant heapify')

# # For small values of n
# ax.plot(X_real[:30], Y_real[:30], 'm', label='Real heapify')
# ax.plot(X_variant[:30], Y_variant[:30], 'y', label='Variant heapify')

plt.legend()
plt.title('Heapify for small values of n')
plt.xlabel("N")
plt.ylabel("Time taken")
plt.show()
# plt.savefig("Small.pdf")

