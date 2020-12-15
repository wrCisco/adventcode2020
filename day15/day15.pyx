cpdef (int, int) run():
    cdef list nums, prevs
    cdef int last, turn, i, first

    with open('input.txt') as fh:
        nums = [int(n) for n in fh.read().split(',')]

    prevs = [0] * 30000000
    for i, n in enumerate(nums, 1):
        prevs[n] = i
    last = nums[-1]
    for turn in range(len(nums), 30000000):
        prevs[last], last = turn, turn - prevs[last] if prevs[last] else 0
        if turn == 2019:
            first = last
    return first, last
