#==========================================
# Title:  Codility FrogJmp
# Author: Steven Cao
# Date:   2 Feb 2023
# Score:  100/100
# Errors: Not an error, but need to int(<float>) before return due to the expected return type
#==========================================

import unittest

def solution(X, Y, D):
    dist = Y - X
    if dist % D != 0: #no incomplete jumps
        return int(dist/D) + 1
    return int(dist/D) #return type int() because '/' makes it a float


test = (10,85,30,3), (125,1111,33,30)

class TestStringMethods(unittest.TestCase):

    def test_split(self):
        for ele in test:
            self.assertEqual(solution(ele[0], ele[1], ele[2]), ele[3])
        #check the result against the expected number of gaps

if __name__ == '__main__':
    unittest.main()
