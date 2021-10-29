from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver('GLOP')

def main():
    print('Griasde servus')

    x1 = solver.NumVar(0, solver.infinity(), 'x1')
    x2 = solver.NumVar(0, solver.infinity(), 'x2')

    solver.Add(x1 + 4 * x2 <= 160)
    solver.Add(x1 + 2 * x2 <= 110)
    solver.Add(x1 + x2 <= 100)

    solver.Maximize(x1 + 3 * x2)

    status = solver.Solve();

    if status == solver.OPTIMAL:
        print('Lösung: ', solver.Objective().Value())
        print('x1: ', x1.solution_value(), ', x2: ', x2.solution_value())
    else:
        print('Keine Lösung diggi')

if __name__ == '__main__':
    main()