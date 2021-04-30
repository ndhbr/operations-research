from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver('GLOP')


def main():
    # Variables
    verticesSize = 8;
    streetSize = 12;
    # Cost Matrix
    C = [[0 for x in range(verticesSize)] for y in range(verticesSize)]
    C[0][1] = 6;
    C[0][2] = 9;
    C[0][4] = 5;
    C[1][0] = 6;
    C[1][3] = 5;
    C[1][4] = 9;
    C[1][5] = 8;
    C[2][0] = 9;
    C[2][4] = 7;
    C[2][6] = 11;
    C[3][1] = 5;
    C[3][5] = 4;
    C[4][0] = 5;
    C[4][1] = 9;
    C[4][2] = 7;
    C[4][5] = 9;
    C[4][6] = 8;
    C[5][1] = 8;
    C[5][3] = 4;
    C[5][4] = 9;
    C[5][7] = 6;
    C[6][2] = 11;
    C[6][4] = 8;
    C[6][7] = 10;
    C[7][5] = 6;
    C[7][6] = 10;
    X = [0 for x in range(streetSize)]

    x = solver.IntVar(0, solver.infinity(), 'x')
    y = solver.IntVar(0, solver.infinity(), 'y')

    # Constraints
    solver.Add(x + 3 * y <= 9)
    solver.Add(-x + 2 * y <= 2)

    # Target function
    solver.Minimize(sum(x))

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
