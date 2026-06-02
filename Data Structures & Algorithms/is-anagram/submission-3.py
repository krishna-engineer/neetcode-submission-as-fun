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
            bool: Indicating if two strings are anagrams
        
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
            > For each foo char, check count of that in foo & bar
                - If count is same, move to next char
                - If count is not same, return False
            > But count() too is O(n) and if performed for each char twice, it'll be O(n square) time complexity
            > Thogu space complexity will be O(1)
        
        Logic 2.1:
            > Instead of using count(), we can build our own freq counter using dict which is O(n)
            > Comparison of 2 dicts is again O(n)
                * But because input is always lower case letters, it'll be O(26) = O(1), irrespective of length of foo and bar 

        Logic 3:
            > What if we sort two strings, and do comparison
            > Sorting will be O(n.logn)
            > And space complexity too will be O(n)
        '''

        # This is a cheap condition that can eliminate freq dict creation for many cases
        if len(foo) != len(bar):
            return False
        
        freq_counter_foo = {}
        freq_counter_bar = {}

        for char_foo in foo:
            freq_counter_foo[char_foo] = freq_counter_foo.get(char_foo, 0) + 1
        
        for char_bar in bar:
            freq_counter_bar[char_bar] = freq_counter_bar.get(char_bar, 0) + 1

        return freq_counter_foo == freq_counter_bar
        # sorted_list_foo = sorted(foo)
        # sorted_list_bar = sorted(bar)

        # return sorted_list_foo == sorted_list_bar
        