# The shortestWay method finds the minimum number of times the `source` string must be 
# used as a subsequence to form the `target`.

# Two-pointer Approach:
# - Iterate through `target` while scanning `source` for matching characters.
# - If a character in `target` matches `source`, move the `target` pointer forward.
# - If no match is found in an entire scan, return -1 (target cannot be formed).
# - Repeat the process until `target` is fully covered, counting the number of scans.

# TC: O(n * m) - Worst case iterating through `source` multiple times.
# SC: O(1) - Constant space used.


class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        s_len, t_len = len(source), len(target)
        ans,t_reader = 0,0
        
        while t_reader < t_len:
            s_reader = 0
            flag = False
            while s_len > s_reader and t_len > t_reader:
                if source[s_reader] == target[t_reader]:
                    t_reader += 1
                    flag = True
                s_reader += 1
            if not flag:
                return -1
            ans += 1
        return ans