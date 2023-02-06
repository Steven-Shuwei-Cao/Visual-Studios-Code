
def solution(A, R):
    unique = []; free = 0
    for i in range(len(A)-R):
        left = (A[:i] + A[i+R:])
        count = 0
        for i in left:
            if i not in unique:
                unique.append(i)
                count += 1
        free = max(free, count)
    print(free)
solution([1,2,2,3,2,1], 3)
solution([1,2,2,2,2,1], 3)
solution([1, 100000, 1], 3)