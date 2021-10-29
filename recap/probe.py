from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver('GLOP')

def main():
    print('Calculating...')

    x1 = solver.IntVar(0, solver.infinity(), 'x1')
    x2 = solver.IntVar(0, solver.infinity(), 'x2')

    solver.Add(2 * x2 <= 20)
    solver.Add(2 * x1 + 10 * 2 <= 66)
    solver.Add(x1 - 2 * x2 <= 20)
    solver.Add(-4 * x1 - 2 * x2 >= -44)
    
    solver.Minimize(2 * x1 - 2 * x2)

    status = solver.Solve()

    if (status == pywraplp.Solver.OPTIMAL):
        print('Result: ', solver.Objective().Value())
        print('x1: ', x1.solution_value(), ', x2: ', x2.solution_value())

if __name__ == '__main__':
    main()