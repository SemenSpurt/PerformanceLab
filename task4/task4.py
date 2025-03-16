## Task 4

import sys
import numpy as np


def calc(nums: list) -> int:
    return sum([int(abs(each - round(np.mean(nums), 0))) for each in nums])


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        nums = [int(i.strip()) for i in f.readlines()]
    print(calc(nums))