from time import time
import logging


class Stack:

    # Initializes necessary parameters for the stack
    def __init__(self, size=-1):
        self.stack = None
        self.top = None
        self.size = -1
        self.current_size = -1
        
    def get_val(self):
        return self.top.get_data()

    def set_size(self, size):
        self.size = size

    # Pusing the element to the top of the stack
    # e1 -> e2 -> ... -> en -> None => ... en -> en+1 -> None
    def push(self, val):
        if self.size != -1:
            if self.current_size+1 >= self.size:
                print('Overflow')
                return

        if self.current_size == -1:
            self.stack = self._StackNode(val)
            self.current_size += 1
            return
        
        node = self._StackNode(val)
        
        nelem = self.stack
        while nelem.get_next():
            nelem = nelem.get_next()

        nelem.set_next(node)
        
        self.top = node
        self.current_size += 1

    # Popping the last element
    # e1 -> e2 -> ... en -> None => e1 -> e2 -> ... en-1 -> None
    def pop(self):
        if self.current_size == -1:
            print('Underflow')
            return None

        val = self.top.get_data()

        if self.current_size == 0:
            self.stack = None
            self.current_size -= 1
            return val
        
        nelem = self.stack
        while nelem.get_next().get_next():
            nelem = nelem.get_next()
        nelem.set_next(None)
        self.top = nelem

        self.current_size -= 1
        
        return val

    # Intentionally named different than qn according to python
    # Convention
    def is_empty(self):
        if self.current_size == -1:
            return True
        return False

    # Node class
    class _StackNode:
        def __init__(self, data=0):
            self.__data = data
            self.__next = None

        def get_val(self):
            return self.__data

        def set_data(self, data):
            self.__data = data

        def get_data(self):
            return self.__data

        def set_next(self, node):
            self.__next = node

        def get_next(self):
            return self.__next


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filename='times.log')
    K = 10 ** 6

    logging.info('Reporting times for pushing elements')
    
    stack = Stack()
    sum = 0
    for i in range(5):
        start = time()
        stack.push(i)
        t = time() - start

        logging.info(f'Round {i+1}: {t}')
        
        sum += t
        
    logging.info(f'Average time: {(sum/5)*K} microsecs')

    logging.info('\n')
    
    logging.info('Reporting times for poppping elements')
    sum = 0
    count = 1
    while not stack.is_empty():
        start = time()
        print('Popping', stack.pop())
        t = time() - start

        logging.info(f'Round {count}: {t}')

        sum += t
        count += 1
        
    logging.info(f'Average time: {(sum/5)*K} microsecs')

    # Case for underflow and overflow
    stack.set_size(5)
    
    for i in range(6):
        stack.push(5)
        
    for i in range(6):
        print("Popping: ", stack.pop())
        
