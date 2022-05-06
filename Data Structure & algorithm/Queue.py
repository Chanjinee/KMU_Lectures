# [ 문제 2-큐 ]
class CircularQueue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.items = [0] * MAX_QSIZE
    def isEmpty(self): return self.front == self.rear
    def isFull(self): return self.front == (self.rear+1)%MAX_QSIZE
    
    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear+1)%MAX_QSIZE
            self.items[self.rear] = item
        
    def dequeue(self):
        if not self.isEmpty():
            self.items[self.front+1] = 0 # 가장 처음의 값을 0으로 바꿔줌
            self.front = (self.front+1)%MAX_QSIZE
            return self.items[self.front]
        
    def peek(self):
        if not self.isEmpty():
            self.items[(self.front+1)%MAX_QSIZE]
    
    def size(self):
        return (self.rear - self.front + MAX_QSIZE)%MAX_QSIZE
    
    def display(self):
        return print(self.items)
    
    
# 실행
if __name__ == '__main__':
    q = int(input('MAX QSIZE> '))
    n = int(input('연산횟수> '))
    MAX_QSIZE = q
    cirqueue = CircularQueue()

    for i in range(n): # 연산횟수번 반복
        inputs = input('inputs> ').split()
        
        if not cirqueue.isFull(): # overflow
            operation = inputs[0]
            if operation == 'I':
                item = inputs[1]
                cirqueue.enqueue(item)
            if operation == 'D':
                if not cirqueue.isEmpty(): # underflow
                    cirqueue.dequeue()
                else:
                    print('underflow', end='')
                    break
            if operation == 'P':
                cirqueue.display()
            
        else:
            print('overflow', end='')
            cirqueue.display()
            break
