#==========================================
# Title:  Codility CyclincRotation
# Author: Steven Cao
# Date:   1 Feb 2023
# Score:  100/100
# Errors: Ran into minor errors when K = K % len(A) was mistakenly written as K = len(A) % K
#==========================================

import unittest

def solution(A, K):
    if K == 0 or K == len(A) or not A: #no rotation/full complete rotation/empty array => return original array
        return A
    if K > len(A): #if k > len(A), we only need the remainder since it will loop around
        K = K % len(A) 
    #print(A, K, len(A))
    head = A[:len(A)-K]
    tail = A[len(A)-K:]
    ans = tail + head
    #print(head, tail)
    return ans

test = ([3, 8, 9, 7, 6], 3, [9, 7, 6, 3, 8]), ([0, 0, 0], 1, [0, 0, 0]), ([1, 2, 3, 4], 4, [1, 2, 3, 4]), ([5, -1000], 1,  [-1000, 5]), ([1, 1, 2, 3, 5], 42, [3, 5, 1, 1, 2])

class TestStringMethods(unittest.TestCase):

    def test_split(self):
        for ele in test:
            self.assertEqual(solution(ele[0], ele[1]), ele[2])
        #check the result against the expected number of gaps

if __name__ == '__main__':
    unittest.main()
