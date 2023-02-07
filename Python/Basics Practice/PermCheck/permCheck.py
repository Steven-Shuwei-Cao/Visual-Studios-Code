#==========================================
# Title:  Codility PermCheck
# Author: Steven Cao
# Date:   2 Feb 2023
# Score:  100/100
# Errors: N/A
#==========================================

import unittest

def solution(A):
    check = set()
    for i in A:
        if i not in check:
            check.add(i) #add unique elements to the set
        else:
            return 0 #if duplicates exist, it is not a permutation
    if max(check) == len(check): #permutation length should equal to the max num
        return 1
    return 0

test = ([4,1,3,2],1), ([4,1,3], 0)

class TestStringMethods(unittest.TestCase):

    def test_split(self):
        for ele in test:
            self.assertEqual(solution(ele[0]), ele[1])
        #check the result against the expected number of gaps

if __name__ == '__main__':
    unittest.main()
