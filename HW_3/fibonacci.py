import math

def naive_recursive(length):
    if(length <= 1):
        return length
    else:
        return (naive_recursive(length-1) + naive_recursive(length-2))

def bottom_up(length):
    arr = []
    arr.append(0)
    arr.append(1)

    i = 0
    
    for i in range(2, length+1):
        arr.append(arr[i-1]+arr[i-2])

    return arr[i]

def closed_form(length):
    golden = (1+math.sqrt(5))/2.0
    return int(math.pow(golden, length)/ math.sqrt(5))

def matrix_method(length): 
    F = [[1, 1], 
         [1, 0]] 
    if (length == 0): 
        return 0
    power(F, length - 1) 
      
    return F[0][0] 
  
def multiply(F, M): 
  
    x = (F[0][0] * M[0][0] + 
         F[0][1] * M[1][0]) 
    y = (F[0][0] * M[0][1] +
         F[0][1] * M[1][1]) 
    z = (F[1][0] * M[0][0] + 
         F[1][1] * M[1][0]) 
    w = (F[1][0] * M[0][1] + 
         F[1][1] * M[1][1]) 
      
    F[0][0] = x 
    F[0][1] = y 
    F[1][0] = z 
    F[1][1] = w 
  
def power(F, n): 
  
    M = [[1, 1], 
         [1, 0]] 

    for i in range(2, n + 1): 
        multiply(F, M) 
  
RUNNING_TIME = 3

f = open("diff_file.txt", "w")

from time import clock
from time import time
start = clock()

print('hello')

# f.write("Time in nanoseconds (approx)\n\n")

_space = ' '*13
__space = ' '*20
FIXED_TIME = 10 #in seconds

# f.write(f"{_space}NaiveRecursive{_space}Bottom up{_space}Closed fom{_space}Matrix method{_space}\n")
# f.write('_'*180)
# f.write('\n')

for i in range(1, 100, 1):
    if clock()-start > 10:
	break

    f.write(f'{i}{__space}')

    check_pt0 = time()
    naive_recursive(i)
    f.write(f'{int((time()-check_pt0)*10e9)}{_space}')
    
    check_pt1 = time()
    bottom_up(i)
    f.write(f'{int((time()-check_pt1)*10e9)}{_space}')

    check_pt2 = time()
    closed_form(i)
    f.write(f'{int((time()-check_pt2)*10e9)}{_space}')

    check_pt3 = time()
    matrix_method(i)
    f.write(f'{int((time()-check_pt3)*10e9)}')

    f.write("\n")

# f.write(f"\n\nTotal computation time:{clock()-start} seconds")

f.close()
