#==========================================
# Title:  Codility BinaryGap
# Author: Steven Cao
# Date:   7 Jan 2011
# Score:  100/100
#==========================================

import unittest

def solution(N):
    bin_n = bin(N)[2:]
    lowest = 0; temp = 0
    
    #iterative approach
    for ele in bin_n:
        if ele == bin(0)[2:]:
            temp += 1
            continue
        if temp > lowest:
            lowest = temp
        temp = 0
    
    #print(bin_n, lowest)
    return lowest

test = [1041, 5], [15, 0], [32, 0], [113, 3]

class TestStringMethods(unittest.TestCase):

    def test_split(self):
        for ele in test:
            self.assertEqual(solution(ele[0]), ele[1])
        #check the result against the expected number of gaps

if __name__ == '__main__':
    unittest.main()