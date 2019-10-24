class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        return self.items[-1]

    def top(self):
        return self.items[-1]
        
    def size(self):
        return len(self.items)
        
def main():
    s = Stack()
    print(s.is_empty())
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.size())
    print(s.top())
    print(s.is_empty())
    while not s.is_empty():
        print(s.pop())

if __name__ == '__main__':
    main()