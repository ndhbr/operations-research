import sys

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.distance = sys.maxsize
        self.visited = False
        self.previous = None

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])


class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost=0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[to], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous


def shortest(v, path):
    ''' Make shortest path from v.previous '''
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return


def ret_1st_ele(tuple):
    return tuple[0]

def dijkstra(graph, start, target):
    start.set_distance(0)
    unvisited_queue = [(v.get_distance(), v) for v in graph]

    while len(unvisited_queue):
        # Pops the node with the smallest distance
        uv = min(unvisited_queue, key=ret_1st_ele)
        unvisited_queue.remove(uv)

        current = uv[1]
        current.set_visited()

        for next in current.adjacent:
            # if visited, skip
            if next.visited:
                continue

            new_dist = current.get_distance() + current.get_weight(next)

            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)

        # Rebuild queue
        unvisited_queue = [(v.get_distance(), v) for v in graph if not v.visited]

if __name__ == '__main__':
    g = Graph()

    g.add_vertex('1')
    g.add_vertex('2')
    g.add_vertex('3')
    g.add_vertex('4')
    g.add_vertex('5')
    g.add_vertex('6')
    g.add_vertex('7')
    g.add_vertex('8')
    g.add_vertex('9')
    g.add_vertex('10')

    g.add_edge('1', '2', 138)
    g.add_edge('1', '4', 190)
    g.add_edge('1', '5', 52)
    g.add_edge('2', '3', 55)
    g.add_edge('3', '4', 93)
    g.add_edge('3', '8', 148)
    g.add_edge('4', '9', 42)
    g.add_edge('8', '9', 108)
    g.add_edge('9', '6', 96)
    g.add_edge('9', '10', 29)
    g.add_edge('10', '7', 75)
    g.add_edge('7', '6', 16)
    g.add_edge('7', '5', 119)
    g.add_edge('5', '6', 76)
    print('Graph data:')
    
    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print('(%s, %s, %3d)' % (vid, wid, v.get_weight(w)))
    
    print('Dijkstra:')
    dijkstra(g, g.get_vertex('1'), g.get_vertex('7'))

    target = g.get_vertex('7')
    path = [target.get_id()]
    shortest(target, path)
    print('Distance to 7: %3d' % (target.get_distance()))
    print('The shortest path: %s' % (path[::-1]))