## Task 1

import sys


def path_calc(n: int , m: int ) -> int:
    if n < 1 or m < 1:
        raise ValueError('Arguments must be positive integers')

    else:
        seq = list(range(1, n + 1))
    
        path = [1]
        nx_el = m - 1
        n_elem = len(seq)

        while seq[nx_el % n_elem] != 1:
            
            path.append(str(seq[nx_el % n_elem]))
            nx_el += m - 1
            
        else:
            return int("".join([str(i) for i in path]))


if __name__ == "__main__":
    print(path_calc(*[int(arg) for arg in sys.argv[1:3]]))