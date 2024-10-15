class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = []
        running_sum = 0

        for num in nums:
            running_sum += num
            prefix_sum.append(running_sum)

        difference = float('inf')
        index = 0
        m = len(prefix_sum)

        for i in range(1, m):
            operand1 = prefix_sum[i - 1] // i
            operand2 = (running_sum - prefix_sum[i - 1]) // (m - i)

            if abs(operand1 - operand2) < difference:
                difference = abs(operand1 - operand2)
                index = i - 1

        return n - 1 if running_sum // n < difference else index