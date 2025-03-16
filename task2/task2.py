## Task 2

import sys


def locate_point(center: list, radius: float, point: list) -> int:
    point_to_center_dist = sum(abs(a - b) for a, b in zip(center, point))
    point_to_edge_distance = point_to_center_dist - radius
    
    if point_to_edge_distance < 0:
        return 1
    
    elif point_to_edge_distance > 0:
        return 2
    
    else: 
        return 0


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        [c, r] = f.readlines()
        center = [float(i) for i in c.split()]
        radius = float(r)

    with open(sys.argv[2]) as f:
        points = [[float(j) for j in i.split()] for i in f.readlines() if i != ""]

    for point in points:
        print(locate_point(center, radius, point))
