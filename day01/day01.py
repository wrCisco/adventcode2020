#!/usr/bin/env python3


def run():
    with open('input.txt', encoding='utf-8') as fh:
        nums = [int(num.rstrip()) for num in fh.readlines()]

    checks = set()
    for num in nums:
        if num in checks:
            print(num * (2020 - num))  # first answer
            break
        checks.add(2020 - num)

    sums = {}
    checks = set()
    for i, num in enumerate(nums):
        for num2 in nums[i+1:]:
            if num + num2 < 2020:
                sums[num + num2] = [num, num2]
                checks.add(2020 - (num + num2))
    for num in nums:
        if num in checks:
            print(num * sums[2020-num][0] * sums[2020-num][1])  # second answer method 1
            break

    snums = sorted(nums)
    for i, num in enumerate(snums):
        j = i + 1
        n = len(nums) - 1
        while j < n:
            s = num + snums[j] + snums[n]
            if s == 2020:
                print(num * snums[j] * snums[n])  # second answer method 2
                return
            elif s < 2020:
                j += 1
            else:
                n -= 1


if __name__ == '__main__':
    run()
