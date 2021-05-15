from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver('GLOP')


def main():
    # Variables
    x1 = solver.IntVar(0, solver.infinity(), 'x')
    x2 = solver.IntVar(0, solver.infinity(), 'x2')

    # Constraints
    solver.Add(10 * x1 + 18 * x2 <= 109)
    solver.Add(21 * x1 - 24 * x2 <= 44)
    solver.Add(5 * x1 + 9 * x2 <= 54)
    solver.Add(7 * x1 - 8 * x2 <= 14)

    # Instanzen
    solver.Add(x1 <= 5)
    solver.Add(x2 >= 4)
    solver.Add(x1 <= 3)


    # Target function
    solver.Maximize(7 * x1 + 10 * x2)

    # Solve
    status = solver.Solve()
    
    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print('Objective value =', solver.Objective().Value())
        print('x1 =', x1.solution_value())
        print('x2 =', x2.solution_value())
    else:
        print('The problem does not have an optimal solution.')


if __name__ == '__main__':
    main()
