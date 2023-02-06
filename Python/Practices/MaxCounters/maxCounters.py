#==========================================
# Title:  Codility MaxCounters
# Author: Steven Cao
# Date:   6 Feb 2023
# Score:  77/100
# Errors: While it works, the performance could be improved.
#==========================================

import unittest

def solution(N, A):
    counters = N * [0]; big = 0
    for i in A:
        if i <= N:
            counters[i-1] += 1
            if counters[i-1] > big:
                big = counters[i-1]
        else:
            counters = N * [big]
        #print(counters, big)
    return counters
    
test = (5, [3,4,4,6,1,4,4], [3,2,2,4,2]), (5, [3,4,4,6,1,4,4], [3,2,2,4,2])

class TestStringMethods(unittest.TestCase):

    def test_split(self):
        for ele in test:
            self.assertEqual(solution(ele[0], ele[1]), ele[2])
        #check the result against the expected number of gaps

if __name__ == '__main__':
    unittest.main()
