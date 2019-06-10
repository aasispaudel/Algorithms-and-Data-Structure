class Node:
    def __init__(self):
        self.val = 0
        self.next = None

        
first_node = Node()
first_node.val = 0
first_node.next = None

def push_back(val):
    node = Node()
    node.val = val

    f_node = first_node
    
    while f_node.next:
        f_node = f_node.next

    f_node.next = node
    node.next = None

def print_list():
    f_node = first_node

    while f_node.next:
        print(f_node.val, end=', ')
        f_node = f_node.next

    print(f_node.val)

    print()
        
    
for i in range(1, 5):
    push_back(i)
print(first_node.val)
    
print_list()
