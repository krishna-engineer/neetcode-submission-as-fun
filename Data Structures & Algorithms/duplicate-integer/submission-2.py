class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        > This function accepts a list of integers.
        > It checks if any list item (integer) appears more than once in the list.
            - If more than once, return True
            - Else return False
        > E.g.:
            - [1,2,3,3] => True
            - [2,3,4,5] => False
        """

        '''
        Logic buidling approaches:
        1. Using set():
            > We create deduplicated list of nums (using set)
            > If length of deduplicated list is less than original list, 
              then it proves that original list had repeated numbers
            > Time complexity: O(n) for set operation
            > Space complexity: O(n), as new unique list will be created

        2. Using count():
            > For each element of list, run count() of that item on list.
            > If item count is more than 1, it means list has duplicates
            > Time complexity: This will become O(n2)
                - Each loop item, so O(n)
                - count funtion check against each item of loop, so (n)
            > Space complexity: O(1) as no new data is being created in memory

        3. Maintaing a set of traversed elements:
            > For each element of list, add the element in a set
            > Before adding to set, check if element already exists.
            > Time complexity: O(1) Avg case 
            > Space complexity: O(1) Avg case
            > Imp: This will be best approach for cases like [1,1,2,3], where duplication occurs early
        
        Going ahead with 3rd approach
        '''
        traversed_items = set()
        for num in nums:
            if num not in traversed_items:
                traversed_items.add(num)
            else:
                return True
        return False
        # unique_nums = set(nums)
        # return len(unique_nums) < len(nums)


