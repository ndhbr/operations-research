"""Loading distance matrix, Tutorial 6, Excercise 2b"""
from collections import namedtuple
from scipy.spatial import distance_matrix

Point = namedtuple('Point', 'x, y')

def read_nodes():
    """Read the nodes from bier127.tsp"""
    with open('bier127.tsp', 'r') as file:
        lines = file.readlines()

    # first 6 lines are irrelevant descriptions
    # last line is also irrelevant
    lines = lines[6:-1]

    # each line contains 3 sections: node number, x coordinate, y coordinate
    lines_split = [line.split() for line in lines]
    nodes = [Point(int(split[1]), int(split[2])) for split in lines_split]
    return nodes


def main():
    """Read the nodes, compute the distance matrix, and print it"""
    nodes = read_nodes()
    d = distance_matrix(nodes, nodes)
    print('Number of nodes: {0}'.format(len(nodes)))
    print('First 5 nodes: {0}'.format(nodes[:5]))
    print('Distance matrix:\n{0}'.format(d))


if __name__ == '__main__':
    main()
