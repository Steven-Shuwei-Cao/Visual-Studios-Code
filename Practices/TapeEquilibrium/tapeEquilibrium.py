#==========================================
# Title:  Codility TapeEquilibrium
# Author: Steven Cao
# Date:   2 Feb 2023
# Score:  100/100
# Errors: N/A
#==========================================

import unittest

def solution(A):
    total = sum(A)
    left = 0
    diff = float('inf') #initialize diff as infinity for later min() usage
    for i in A[:-1]:
        left += i
        #difference = right - left
        #right = total - left
        #diff = total - left - left
        diff = min(abs(total-2*left), diff)
    
    return diff
    

test = ([3,1,2,4,3],1), ([8,8,8,8,8,6,6,6,6,6,6,6],2), ([1,1], 0)

class TestStringMethods(unittest.TestCase):

    def test_split(self):
        for ele in test:
            self.assertEqual(solution(ele[0]), ele[1])
        #check the result against the expected number of gaps

if __name__ == '__main__':
    unittest.main()
