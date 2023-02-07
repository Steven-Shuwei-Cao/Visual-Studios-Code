#==========================================
# Title:  Codility MissingInteger
# Author: Steven Cao
# Date:   7 Feb 2023
# Score:  100/100
# Errors: N/A
#==========================================

import unittest

def solution(A):
    N = len(A)
    A = set(A)
    for i in range(1, N + 2):
        if i not in A:
            return i

test = ([1, 3, 6, 4, 1, 2],5), ([8,6,4,2,7,5,1], 3), ([-1, -3], 1)

class TestStringMethods(unittest.TestCase):

    def test_split(self):
        for ele in test:
            self.assertEqual(solution(ele[0]), ele[1])
        #check the result against the expected number of gaps

if __name__ == '__main__':
    unittest.main()
