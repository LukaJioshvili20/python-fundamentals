"""
ვიყენებ:
python 3 ( python 3.9 ).
compiler: https://leetcode.com/problems/rotate-function/
ანალიზი:
time complexity - o(N)
"""

class Solution:
    def maxRotateFunction(self, A):
        sum_A = sum(A)
        n = len(A)
        cur_sum = sum(i * n for i, n in enumerate(A))
        max_sum = cur_sum

        for i in range(1, n):
            cur_sum = cur_sum + sum_A - n * A[-i]
            if (cur_sum > max_sum):
                max_sum = cur_sum

        return max_sum