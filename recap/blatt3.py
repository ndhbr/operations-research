from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver('GLOP')

def mul(x, y):
    """Compute the inner product of vectors x and y of same length

    Example: x = [1, 2, 3], y = [3, 4, 5], mul(x, y) = 1*3+2*4+3*5
    x = [1,2,3], y = [obj1, obj2, obj3], mul(x, y) = 1*obj1 + 2*obj2 + 3*obj3
    """
    return sum(x_i * y_i for x_i, y_i in zip(x, y))

def main():

    x1 = solver.IntVar(0, solver.infinity(), 'x1')
    x2 = solver.IntVar(0, solver.infinity(), 'x2')
    x3 = solver.IntVar(0, solver.infinity(), 'x3')
    x4 = solver.IntVar(0, solver.infinity(), 'x4')
    x5 = solver.IntVar(0, solver.infinity(), 'x5')

    solver.Add(5 * x1 <= 10)
    solver.Add(6 * x2 <= 12)
    solver.Add(6 * x3 <= 12)
    solver.Add(8 * x4 <= 16)
    solver.Add(x5 <= 2)
    solver.Add(5 * x1 + 4 * x2 + 2 * x3 + 2 * x4 + 2 * x5 <= 15)

    solver.Maximize(3 * x1 + 6 * x2 + 6 * x3 + 8 * x4 + x5)

    status = solver.Solve()

    if (status == pywraplp.Solver.OPTIMAL):
        print('Solution:')
        print('Whole: ', solver.Objective().Value())
        print('x1: ', x1.solution_value(), ', x2: ', x2.solution_value(), ', x3: ', x3.solution_value(),
            ', x4: ', x4.solution_value(), ', x5: ', x5.solution_value())
    else:
        print('Utzi')

def test():
    # set up the model
    x = [solver.IntVar(lb=0, ub=2, name=f'x_{i}')
         for i in range(1, 6)]
    c = [3, 6, 6, 8, 1]
    a = [5, 4, 2, 2, 2]
    b = 15
    solver.Add(mul(a, x) <= b)
    f = mul(c, x)
    solver.Maximize(f)

    # solving
    result_status = solver.Solve()

    # print result
    for x_i in x:
        print('{0}: {1}'.format(x_i.name(), x_i.solution_value()))

if __name__ == '__main__':
    test()