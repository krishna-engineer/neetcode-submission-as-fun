class Solution:
    def isValid(self, s: str) -> bool:
        """
        Input s is a string consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

        s is valid if and only if:
            > Every open bracket is closed by the same type of close bracket.
            > Open brackets are closed in the correct order.
            > Every close bracket has a corresponding open bracket of the same type.

        Examples:
            1.  "[]"    => True
            2. "([{}])" => True
            3. "[(])"   => False
        """
        
        '''
        Logic 1:
            - Create two separate lists of opening and closing paranthesis in order they appear
            - len of both list should be same, if not, return False
            - For each item of closed lists, do a pop operation on open list, if both items are same, it's right opening and closing

        Logic 2:
            - Traverse through each char, keep adding open parenthesis to a list, the moment closed parenthesis is found, do immmediate pop on open parenthesis
        '''


        # list_valid_chars = ['(', ')', '{', '}', '[', ']']
        parenthesis_map = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        opened_parenthesis_in_order = []
        for char in s:
            # if char not in list_valid_chars:
            #     return False

            if char in parenthesis_map:
                # For opened parenthesis, add it to respective list
                opened_parenthesis_in_order.append(char)
                continue
            
            '''
            For closed parenthis: 
                > first make sure that there's indeed an open bracket of any type
            '''
            if len(opened_parenthesis_in_order) < 1:
                return False 

            poped_from_open = opened_parenthesis_in_order.pop()
            if char != parenthesis_map[poped_from_open]:
                return False
        
        # Eventually all items from opened_parenthesis_in_order should be popped
        if len(opened_parenthesis_in_order) > 0:
            return False
        return True

