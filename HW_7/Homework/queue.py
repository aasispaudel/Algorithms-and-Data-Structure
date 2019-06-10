import stack


'''
The way enqueue works is:
Case: 1 element
Stack 1 -> e1 Stack 2 -> empty

Pop element from stack 1 and add to stack 2
Add new element to stack 1 
Stack 1 -> e2 Stack 2 -> e1

Add popped element from stack 2 to stack 1
Stack 1 -> e2-> e1 Stack 2 -> empty

Case: multiple elements (consider n elements are in require order)
Stack 1 -> en Stack 2 -> empty

Pop elements from stack 1 and add to stack 2
Stack 1 -> empty Stack 2 -> en (reversed)

Add the new element to stack 1
Stack 1 -> en+1 Stack 2 -> en (reversed)

Pop elements from Stack 2 and add to Stack 1
Stack 1 -> en+1-> en (Correct order again)

Thus, this method will work for every n :)
'''


class Queue:

    # Initializes the queue parameters
    def __init__(self, size=-1):
        self.size = size
        self.current_size = 0
        
        self.queue = stack.Stack(size)
        self.assistant = stack.Stack(size)
        
    def enqueue(self, val):
        if (self.size != -1):
            if self.current_size >= self.size:
                print('Overflow')
                return

        if self.current_size == 0:
            self.queue.push(val)
            return

        while not self.queue.is_emtpty():
            self.assistant.add(self.queue.pop())

        self.queue.add(val)

        while not self.assistant.is_empty():
            self.queue.add(self.assistant.pop())

        self.current_size += 1
        
    def dequeue(self):
        self.current_size -= 1
        return self.queue.pop()

    def is_empty(self):
        return self.queue.is_empty()

    
if __name__ == '__main__':
    queue = Queue()

    for i in range(5, 10):
        queue.enqueue(i)

    while not queue.is_empty():
        print("Deque: ", queue.dequeue())
        
