#!/usr/bin/env python
# coding: utf-8

# In[8]:


class Stack:
    def __init__(self):        # 생성자
        self.top = []          # top이 클래스의 멤버 변수가 됨
        
    def isEmpty(self): return len(self.top) == 0
    def size(self): return len(self.top)
    def clear(self): self.top = []
        
    def push(self, item):
        self.top.append(item)
        
    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)
    
    def peek(self):
        if not self.isEmpty():
            return self.top[-1]
        
# 괄호 검사        
def checkBrackets(statement):
    stack = Stack()
    size = 0
    flag = "Wrong"
    for ch in statement:                     
        if ch in ('{','[','('):
            size += 1
            stack.push(ch)
        elif ch in ('}',']',')'):
            size += 1
            if stack.isEmpty():
                return (flag, size)
            else:
                left = stack.pop()
                if (ch == "}" and left != "{") or (ch == "]" and left != "[") or (ch == ")" and left != "("):
                    return (flag, size)
    
    if stack.isEmpty():
        flag = "OK"
        return (flag, size)
    else:
        return (flag, size)
    

# main
input_string = input("Enter equation: ")
result = checkBrackets(input_string)
print("%s_%d"%(result[0], result[1]))    

