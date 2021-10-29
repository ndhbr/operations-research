from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver('GLOP')

def main():
    print('Calculating...')

    z = solver.IntVar(0, solver.infinity(), 'z')
    p1 = solver.IntVar(0, solver.infinity(), 'p1')
    p2 = solver.IntVar(0, solver.infinity(), 'p2')
    p3 = solver.IntVar(0, solver.infinity(), 'p3')
    p4 = solver.IntVar(0, solver.infinity(), 'p4')

    solver.Add(p2 - p3 - p4 >= z)
    solver.Add(-p1 + p3 - p4 >= z)
    solver.Add(p1 - p2 + p4 >= z)
    solver.Add(p1 + p2 + p3 + p4 >= 1)
    
    solver.Maximize(z)

    status = solver.Solve()

    if (status == pywraplp.Solver.OPTIMAL):
        print('Result: ', solver.Objective().Value())
        print('p1: ', p1.solution_value(), ', p2: ', p2.solution_value(), ', p3: ', p3.solution_value(), ', p4: ', p4.solution_value())

if __name__ == '__main__':
    main()