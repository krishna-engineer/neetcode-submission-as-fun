class Solution:
    def isAnagram(self, foo: str, bar: str) -> bool:
        """
        This function checks if 2 strings are anagrams, if yes, it returns True else returns False

        Conditions of anagram strings are:
            > An anagram is a string that contains the exact same characters as another string, but the order 
                of the characters can be different.
            > Exact Match: The length of both strings must be identical.
            > Character Frequency: Every letter must appear the same number of times in both strings.

        Args:
            foo: First string
            bar: second string

        Returns:
            bool: Indiating if two strings are anagrams
        
        Examples:
            > "racecar" & "carrace" => True
            > "listen" & "silent"   => True
            > "jar" & "jam"         => False
        """

        if not isinstance(foo, str) or not isinstance(bar, str):
            raise TypeError("Both input must be string")
        
        '''
        Logic 1:
            > First check length of both strings, if not same, return False
                * len() is O(1)
            > Next: Set is a good data structure for "in" operations: 
                * creation of set is O(n)
                * but lookup is O(1)
            > So we can create set of 1st string (foo)
            > For each character from 2nd string (bar), check if it's present in foo

            > Check: This logic will be False Positive for cases like "racecar" -> "racecaa"

        Logic 2:
            > Apart from length check, we also have to make sure that character count is same.
            > For each foo char, check count

        Logic 3:
            > What if we sort two strings, and do comparison
            > Sorting will be O(n.logn)
        '''

        if len(foo) != len(bar):
            return False
        
        sorted_list_foo = sorted(foo)
        sorted_list_bar = sorted(bar)

        if sorted_list_foo == sorted_list_bar:
            return True
        
        return False
        