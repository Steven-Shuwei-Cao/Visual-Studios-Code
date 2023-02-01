#==========================================
# Title:  Codility CyclincRotation
# Author: Steven Cao
# Date:   7 Jan 2011
# Score:  100/100
#==========================================

import unittest

def solution(A, K):
    K = len(A) % K #if k > len(A), we only need the remainder since it will loop around
    head = A[:K]
    tail = A[K:]
    ans = tail + head
    #print(ans)
    return ans

test = ([3, 8, 9, 7, 6], 3, 
[9, 7, 6, 3, 8]), ([0, 0, 0], 1, [0, 0, 0]), ([1, 2, 3, 4], 4, [1, 2, 3, 4])

class TestStringMethods(unittest.TestCase):

    def test_split(self):
        for ele in test:
            self.assertEqual(solution(ele[0], ele[1]), ele[2])
        #check the result against the expected number of gaps

if __name__ == '__main__':
    unittest.main()
