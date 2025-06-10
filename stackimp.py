class Stack :
    def __init__(self, l):
        self.stack = []
        self.l = l

    def pop1(self):
        if self.is_empty():
            return "stack is empty"
        else:
            return self.stack.pop()

    def push(self, s):
        if self.is_full():
            return "stack is full"
        else:
            self.stack.append(s)
            return self.stack

    def top(self):
        if self.is_empty():
            return "stack is empty "
        else:
            return self.stack[-1]

    def is_empty(self):
     if len(self.stack) == 0:
            return True
     else:
            return False
         
    def is_full(self):
        if len(self.stack) == self.l:
            return True
        else :
            return False 

    def length(self):
        return len(self.stack)
    
s = Stack(10)
print(s.push(3))
print(s.push(4))
print(s.push(5))
print(s)

print(s.length())

print("remove this element", s.pop1())
s.pop1()
s.pop1()
s.pop1()

print(s.top())
print(s.length())