#!/usr/bin/env python
# coding: utf-8

# In[27]:


class DList:
    class Node:
        def __init__(self, item, prev, link):
            self.item = item
            self.prev = prev
            self.next = link
    def __init__(self):
        self.head = self.Node(None, None, None)
        self.tail = self.Node(None, self.head, None)
        self.head.next = self.tail
        self.size = 0
    
    def size(self): return self.size
    def is_empty(self): return self.size == 0
    
    def add(self, pos, item):
        p = self.head
        for i in range(pos):
            p = p.next
        
        t = p.prev
        n = self.Node(item, t, p)
        p.prev = n
        t.next = n
        self.size += 1
    
    def delete(self, pos):
        if self.size < pos:
            return 'Invalid position'
        
        p = self.head
        for i in range(pos):
            p = p.next
        t = p.prev
        q = p.next
        t.next = q
        q.prev = t
        self.size -= 1
    
    def get(self, pos):
        if self.size < pos:
            return 'Invalid position'
    
        p = self.head
        for i in range(pos):
            p = p.next
        return p.item
        
    
    def print(self):
        if self.is_empty():
            print('리스트 비어있음')
        else:
            p = self.head.next
            while p != self.tail:
                if p.next != self.tail:
                    print(p.item, end='')
                else:
                    print(p.item)
                p = p.next

class EmptyError(Exception):
    pass

# 실행
if __name__ == '__main__':
    num = int(input('Number of operations : '))
    List = DList()
    for i in range(num):
        inputs = input("Input : ").split()
        operation = inputs[0]
        if operation == 'A':
            pos = int(inputs[1])
            alphabet = inputs[2]
            List.add(pos, alphabet)
        elif operation == "D":
            pos = int(inputs[1])
            List.delete(pos)
        elif operation == 'G':
            pos = int(inputs[1])
            print(List.get(pos))
        elif operation == 'P':
            List.print()

