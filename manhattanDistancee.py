def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)
    
distance = manhattan_distance(1, 2, 4, 6)
print(distance)
