from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver('GLOP')

def main():
    # Variables
    x = solver.IntVar(0, solver.infinity(), 'x')
    y = solver.IntVar(0, solver.infinity(), 'y')
    w1 = solver.IntVar(0, solver.infinity(), 'w1')
    w2 = solver.IntVar(0, solver.infinity(), 'w2')

    # Constraints
    solver.Add(3 * x + 5 * y + w1 <= 180)
    solver.Add(3 * x + 3 * y + w2 <= 135)

    solver.Maximize(2000 * x + 3000 * y)

    status = solver.Solve()

    if (status == pywraplp.Solver.OPTIMAL):
        print('Solution:')
        print('Objective value =', solver.Objective().Value())
        print('x =', x.solution_value())
        print('y =', y.solution_value())

if  __name__ == '__main__':
    main()