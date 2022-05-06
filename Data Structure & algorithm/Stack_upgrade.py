# [ 문제 1-스택 ] 
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
        else:
            return print("Stack Empty")
            
    def peek(self):
        if not self.isEmpty():
            return print(self.top[-1])
        else:
            return print("Stack Empty")
    
    # duplicate
    def duplicate(self):
        if not self.isEmpty():
            pop_item = self.top.pop(-1) # pop을 한 아이템을 저장
            self.top.append(pop_item) # push 두번
            self.top.append(pop_item)
    
    # upRotate
    def upRotate(self, n):
        if n <= len(self.top):
            pop_item = self.top.pop(-1)
            self.top.insert(-n+1,pop_item) # 맨뒤의 아이템을 pop했기 때문에 +1을 해줌
            
    # downRotate
    def downRotate(self, n):
        if n <= len(self.top):
            pop_item = self.top.pop(-n)
            self.top.insert(len(self.top),pop_item) # 맨뒤에 뒤에서 n번째 요소를 삽입
            
    def print_stack(self):
        print(''.join(self.top[::-1])) # top을 뒤에서부터 출력

        

# 실행
if __name__ == '__main__':
    sig = True # -1이 나오면 정지하기 위함
    stack = Stack()
    while sig:
        inputs = input('inputs> ').split()
        operation = inputs[0]
        if operation == '-1': # -1이면 종료
            sig = False
        elif operation == 'PUSH':
            item = inputs[1]
            stack.push(item)
        elif operation =='POP':
            stack.pop()
        elif operation =='PEEK':
            stack.peek()
        elif operation == 'PRINT':
            stack.print_stack()
        elif operation == 'DownR':
            item = inputs[1]
            stack.downRotate(int(item))
        elif operation == 'UpR':
            item = inputs[1]
            stack.upRotate(int(item))
        elif operation == 'DUP':
            stack.duplicate()
