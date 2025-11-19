from collections import deque

class editor:
    def __init__(self, init_string):
        self.left = deque(init_string)
        self.right = deque([])
    
    def L(self):
        if self.left:
            char = self.left.pop()
            self.right.appendleft(char)
    
    def D(self):
        if self.right:
            char = self.right.popleft()
            self.left.append(char)
    
    def B(self):
        if self.left:
            self.left.pop()
    
    def P(self, char):
        self.left.append(char)
    
    def __str__(self):
        return "".join(self.left) + "".join(self.right)

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    init_string = input()[:-1]
    M = int(input())

    simple_editor = editor(init_string)
    
    for _ in range(M):
        command, *char = input().split()
        if char:
            method = getattr(simple_editor, command)
            method(char[0])
        else:
            method = getattr(simple_editor, command)
            method()
        
    print(simple_editor)
