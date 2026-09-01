def solution_station_1(n):
    if n <= 1:
        return 1
    a, b = 1, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b
