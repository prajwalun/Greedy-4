# The minDominoRotations method finds the minimum number of rotations needed to make all 
# elements in `tops` or `bottoms` uniform.

# Approach:
# - Identify potential target values that appear in the first domino.
# - Check if one of these values is present in all dominoes.
# - If no common value exists, return -1.
# - Otherwise, compute the minimum rotations required to align all dominos.

# TC: O(n) - Single pass to count occurrences.
# SC: O(1) - Constant space usage.

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops) 
        inter = {tops[0], bottoms[0]}
        for i in range(n):
            inter = inter.intersection({tops[i], bottoms[i]})
		# This gives us the finaly common values b/w all the indices. 
        if len(inter) == 0: # Case 1
            return -1
        elif len(inter) == 2: # Case 3
            target = inter.pop()
            m = tops.count(target)
            return min(m, n-m)
        else: # Case 2
            for_tops = for_bottom = 0
            target = inter.pop()
            target_in_tops = tops.count(target)
            target_in_bottoms = bottoms.count(target)
            return n - max(target_in_tops, target_in_bottoms)