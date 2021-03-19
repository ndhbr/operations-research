from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver('GLOP')


def main():
    # Variables
    x = solver.IntVar(0, solver.infinity(), 'x')
    y = solver.IntVar(0, solver.infinity(), 'y')

    # Constraints
    solver.Add(3 * x + 5 * y <= 180)
    solver.Add(3 * x + 3 * y <= 135)

    # Target function
    solver.Maximize(2000 * x + 3000 * y)

    # Solve
    status = solver.Solve()
    
    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print('Objective value =', solver.Objective().Value())
        print('x =', x.solution_value())
        print('y =', y.solution_value())
    else:
        print('The problem does not have an optimal solution.')


if __name__ == '__main__':
    main()
