#==========================================
# Title:  Codility PermMissingElem
# Author: Steven Cao
# Date:   2 Feb 2023
# Score:  100/100
# Errors: N/A
#==========================================

import unittest

def solution(A):
    if not A:
        return 1
    n = len(A) + 1
    expected = n * (n + 1) // 2 #triangular number formula
    #print(expected, sum(A), expected - sum(A))
    return expected - sum(A)
    

test = ([2,3,1,5],4), ([1,2,3,4,5,6,8,9,10], 7), ([], 1), ([2,3,4,5], 1), ([6,3,5,2,4], 1)

class TestStringMethods(unittest.TestCase):

    def test_split(self):
        for ele in test:
            self.assertEqual(solution(ele[0]), ele[1])
        #check the result against the expected number of gaps

if __name__ == '__main__':
    unittest.main()
