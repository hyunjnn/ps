class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, n):
        self.stack.append(n)
        
    def pop(self):
        return self.stack.pop() if self.stack else -1
    
    def size(self):
        return len(self.stack)
    
    def empty(self):
        return 1 if not self.stack else 0
    
    def top(self):
        return self.stack[-1] if not self.empty() else -1
    
N = int(input())
s = Stack()       
for _ in range(N):
    cmd = input().split()
    
    if len(cmd) > 1:
        if cmd[0] == "push":
            s.push(int(cmd[1]))
    else:
        if cmd[0] == "pop":
            print(s.pop())
        elif cmd[0] == "size":
            print(s.size())
        elif cmd[0] == "empty":
            print(s.empty())
        elif cmd[0] == "top":
            print(s.top())