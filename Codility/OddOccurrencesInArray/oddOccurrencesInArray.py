#==========================================
# Title:  Codility OddOccurrencesInArray
# Author: Steven Cao
# Date:   2 Feb 2023
# Score:  100/100
# Errors: N/A
#==========================================

import unittest

def solution(A):
    if not A:
        return 1
    A.sort() #easier to check even/odd with a sorted array
    for i in range(0, len(A), 2):
        if i + 1 == len(A):
            return A[i]
        #print(A[i], A[i+1])
        if A[i] != A[i+1]:
            return A[i]

test = ([9,3,9,3,9,7,9],7), ([5,12,3,56,7,56,3,5,7], 12)

class TestStringMethods(unittest.TestCase):

    def test_split(self):
        for ele in test:
            self.assertEqual(solution(ele[0]), ele[1])
        #check the result against the expected number of gaps

if __name__ == '__main__':
    unittest.main()
