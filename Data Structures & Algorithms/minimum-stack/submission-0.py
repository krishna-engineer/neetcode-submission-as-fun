class MinStack:

    def __init__(self):
        self.stack = []
        self.list_of_minimum = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.list_of_minimum) == 0 or val <= self.list_of_minimum[-1]:
            self.list_of_minimum.append(val)

    def pop(self) -> None:
        popped_item = self.stack.pop()
        if popped_item == self.list_of_minimum[-1]:
            self.list_of_minimum.pop()
        return popped_item
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        """
        This function requires me to retrieve minimum value from stack/list in O(1).
        Python's min() => O(n), so it can't be used here.

        Logic 1:
        - What if we maintain a list of minimum when each push/pop operation is being performed where top item will be current minimum.

        - During push:
            list_minimums = []
            a = []
            a.push(1) => check if list_minimums[-1] > item_being_pushed, if yes, append item_being_pushed to list_minimums
        
        - During pop:
            Scenario 1:
            say a = [22,3,4], list_of_minimum=[22,3]
            popped item from a=4
            new a = [22,3]

            Scenario 2:
            say a = [22,4,3], list_of_minimum=[22,4,3]
            popped item from a=3
            new a = [22,4]

            Scenario 2:
            say a = [22,4,3, 50], list_of_minimum=[22,4,3]
            popped item from a=50
            new a = [22,4,3]

            if item being popped from a is same as last item of list_of_minimum, shrink list_of_minimum
        """
        return self.list_of_minimum[-1]

