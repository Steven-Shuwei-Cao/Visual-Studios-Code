#==========================================
# Title:  Codility FrogRiverOne
# Author: Steven Cao
# Date:   2 Feb 2023
# Score:  100/100
# Errors: N/A
#==========================================

import unittest

def solution(X, A):
    steps = set()
    time = -1
    for i in range (0, len(A)):
        if A[i] not in steps and A[i] <= X: #keep track of each steps' first appearance
            time = i
            steps.add(A[i])
    if len(steps) == X:
        return time
    return -1


test = (5,[1,3,1,4,2,3,5,4],6), (7,[1,3,1,4,2,3,5,4],-1), (2, [2,2,2,2,2],-1), (2,[1,1,1,1],-1), (1,[1],0)

class TestStringMethods(unittest.TestCase):

    def test_split(self):
        for ele in test:
            self.assertEqual(solution(ele[0], ele[1]), ele[2])
        #check the result against the expected number of gaps

if __name__ == '__main__':
    unittest.main()
