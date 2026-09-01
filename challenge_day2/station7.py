import sympy as sp

a, b, c, d, e = sp.symbols("a b c d e")

equations = [
    sp.Eq(a + e*c + d, 12),
    sp.Eq(d + a*e + b, 7.5),
    sp.Eq(e*c, 2),
    sp.Eq(e*d*a + b, 9.5),
    sp.Eq(d + e*b, 6.5),
    sp.Eq(d + c*b, 3),
    sp.Eq(c*b*a + d, -5),
    sp.Eq(d + c, 11),
    sp.Eq(e + c, 4.5),
    sp.Eq(a*d*e + c, 14.5),
]
solution_station_7 = sp.solve(equations, (a, b, c, d, e))

solution_station_7 = [tuple(round(float(value), 1) for value in answer) for answer in solution_station_7]
print(solution_station_7)