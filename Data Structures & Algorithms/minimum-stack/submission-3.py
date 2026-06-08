"""
Logic 2:
- What if when an item is being pushed, along with that item you maintain info of "current_min" -> [(1,1), (3,1), (0,0)]
"""

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:      
        current_min = val
        
        # If current val to push is greater than last_min, then current_min = last_min
        if len(self.stack) > 0 and val > self.stack[-1][1]:
            current_min = self.stack[-1][1]

        self.stack.append((val, current_min))

    def pop(self) -> None:
        return self.stack.pop()[0]
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]

