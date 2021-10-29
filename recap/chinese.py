"""Chinese Postman as LP, Tutorial 6, Excercise 1b

min F(x) = Σ_{ij ∊ E} c_ij x_ij
u.d.N.
∀ ij ∊ E:   x_ij + x_ji ≥ 1
∀ i ∊ V:    Σ_j x_ij - Σ_j x_ji = 0
∀ ij ∊ E:   x_ij ≥ 0
"""
from ortools.linear_solver import pywraplp

SOLVER_STATE = {
    pywraplp.Solver.OPTIMAL: 'OPTIMAL',
    pywraplp.Solver.FEASIBLE: 'FEASIBLE',
    pywraplp.Solver.INFEASIBLE: 'INFEASIBLE',
    pywraplp.Solver.UNBOUNDED: 'UNBOUNDED',
    pywraplp.Solver.ABNORMAL: 'ABNORMAL',
    pywraplp.Solver.NOT_SOLVED: 'NOT_SOLVED'
}

UNDIRECTED_DISTANCES = {
    frozenset(('A', 'B')): 6,
    frozenset(('A', 'C')): 9,
    frozenset(('A', 'E')): 5,
    frozenset(('B', 'D')): 5,
    frozenset(('B', 'E')): 9,
    frozenset(('B', 'F')): 8,
    frozenset(('C', 'E')): 7,
    frozenset(('C', 'G')): 11,
    frozenset(('D', 'F')): 4,
    frozenset(('E', 'F')): 9,
    frozenset(('E', 'G')): 8,
    frozenset(('F', 'H')): 6,
    frozenset(('G', 'H')): 10
}

UNDIRECTED_EDGES = set(UNDIRECTED_DISTANCES.keys())

DIRECTED_EDGES = set(
    edge for i, j in UNDIRECTED_EDGES for edge in [(i, j), (j, i)]
)

VERTICES = set(k for edge in UNDIRECTED_EDGES for k in edge)


def distance(i, j):
    """Get the distance from vertex i to vertex j."""
    return UNDIRECTED_DISTANCES[frozenset((i, j))]


def main():
    """Solve chinese postman as LP"""
    solver = pywraplp.Solver(
        name='solver',
        problem_type=pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

    # one variable per directed edge
    x = {(i, j): solver.IntVar(lb=0, ub=solver.UNBOUNDED, name=f'x_{i}{j}')
         for i, j in DIRECTED_EDGES}

    # each undirected edge is used in at least one direction
    for i, j in UNDIRECTED_EDGES:
        solver.Add(x[i, j] + x[j, i] >= 1)

    # the number of in-going and out-goining edges is the same for every vertex
    for i in VERTICES:
        solver.Add(
            sum(x[i, j] for j in VERTICES if (i, j) in DIRECTED_EDGES)
            -
            sum(x[j, i] for j in VERTICES if (j, i) in DIRECTED_EDGES)
            ==
            0
        )

    f = sum(distance(i, j) * x[i, j] for i, j in DIRECTED_EDGES)
    solver.Minimize(f)

    # solving
    result_status = solver.Solve()

    # print result
    print(SOLVER_STATE[result_status])
    for (i, j), x_ij in x.items():
        print('x_{0}{1} = {2}'.format(i, j, x_ij.solution_value()))


if __name__ == '__main__':
    main()
