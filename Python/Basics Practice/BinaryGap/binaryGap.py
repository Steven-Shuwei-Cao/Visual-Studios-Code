#==========================================
# Title:  Codility BinaryGap
# Author: Steven Cao
# Date:   1 Feb 2023
# Score:  100/100
# Errors: N/A
#==========================================

import unittest

def solution(N):
    bin_n = bin(N)[2:] #convert input to binary
    lowest = 0; temp = 0
    
    #iterative approach
    for ele in bin_n:
        if ele == bin(0)[2:]: #even tho we are only looking for 0's, we still need the binary form to compare types
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
