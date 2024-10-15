"""
ვიყენებ:
python 3 ( python 3.9 ).
compiler: https://leetcode.com/problems/minimum-average-difference/
აღწერა:
იმისათვის რომ თვალყური ვადევნოთ ელემენტებს ამისთვის ვიყენებთ დეკის სტრუქტურას,
რომელიც საშუალებას მოგვცებს რომ მარტივად ვადევნოთ თვალი ელემენტს მარცხენა და მარჯვნივ არსებული
სხვა ელემენტების ჯამს, ამავდროულად ვანახლებთ დეკში ინდექს რომელიც ყოფს მარხენა და მარჯვენა ელემნტებს
როცა პირველ ელემენტს მარხნიდან ვიღებთ დეკიდან მაშინ ვამატებთ მას მარცხნივ არსებულ ჯამს,ვაშორებთ მარჯვნივ არსებული
ჯამიდან და ვამატებთ მარცხნივ ელემენტების რაოდენბოას 1ს და ვაკლებთ
მარჯნვივ არსებულ ელემენტების სიგრძეს
ანალიზი:
time complexity - o(N)
"""

from collections import deque
import sys


class Solution(object):
    def minimumAverageDifference(self, nums):
        n = len(nums)
        if n == 1:
            return 0

        queue = deque(nums[1:])

        left_sum = sum(nums[0: 1])
        right_sum = sum(queue)

        left_length = 1
        right_length = n - 1

        i = 0

        min_average = sys.maxsize
        min_average_idx = None

        while i < n:
            left_average = left_sum // left_length
            if right_length:
                right_average = right_sum // right_length
            else:
                right_average = 0

            diff = abs(left_average - right_average)
            if diff < min_average:
                min_average = diff
                min_average_idx = i

            # თუ დეკი ცარიელია მაშინ შეგვიძლია გავჩერდეთ , ვინიდან უკვე ბოლობში ვართ
            if not queue:
                break
            # უკიდურესი მარცენა ელემენტის მოცილება
            item = queue.popleft()

            # იტერაციის შემდეგ ჯამის განახლება
            left_sum = left_sum + item
            right_sum = right_sum - item

            left_length += 1
            right_length -= 1

            i += 1

        return min_average_idx