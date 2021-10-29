from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver('GLOP')

def main():
    x1 = solver.IntVar(0, solver.infinity(), 'x1')
    x2 = solver.IntVar(0, solver.infinity(), 'x2')

    solver.Add(5 * x1 + 9 * x2 <= 54)
    solver.Add(7 * x1 - 8 * x2 <= 14)
    solver.Add(x2 <= 3)

    solver.Maximize(7 * x1 + 10 * x2)

    status = solver.Solve()

    if (status == pywraplp.Solver.OPTIMAL):
        print('Solution ', solver.Objective().Value())
        print('x1: ', x1.solution_value(), ', x2: ', x2.solution_value())

if __name__ == '__main__':
    main()