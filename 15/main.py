import sys
import cProfile
from itertools import chain


def bfs(paths, graph):
    expanded_paths = []
    all_expanded = True
    print len(paths)
    for p in paths:
        ext_nodes = p.pop()
        # if is not the final node
        if isinstance(ext_nodes, list):
            for n in ext_nodes:
                if n in graph:
                    all_expanded = False
                    expanded_paths.append(p + [n] + [graph[n]])
                else:
                    expanded_paths.append(p + [n])
    if all_expanded:
        return expanded_paths
    return bfs(expanded_paths, graph)


def brute(length):
    graph = gen_graph(length)
    paths = bfs([[1, graph[1]]], graph)
    return len(paths)


def gen_graph(length):
    nodes = {1: [2, 3]}
    depth = 1
    while depth < length:
        nodes = weave(nodes)
        depth += 1
    while depth > 0:
        nodes = unweave(nodes)
        depth -= 1
    return nodes


def filter_not_expanded(nodes):
    expanded = nodes.keys()
    links = set(chain.from_iterable(nodes.values()))
    return [l for l in links if l not in expanded]


def weave(nodes):
    not_expanded = filter_not_expanded(nodes)
    next_node = max(not_expanded) + 1
    for n in not_expanded:
        nodes[n] = [next_node, next_node + 1]
        next_node += 1
    return nodes


def unweave(nodes):
    not_expanded = filter_not_expanded(nodes)
    next_node = max(not_expanded) + 1
    left_tip = not_expanded.pop(0)
    right_tip = not_expanded.pop()
    nodes[left_tip] = [next_node]
    for n in not_expanded:
        nodes[n] = [next_node, next_node + 1]
        next_node += 1
    nodes[right_tip] = [next_node]
    return nodes


def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)


def lattice(length):
    """
    Number of lattice paths is given by the binomial coefficient
    ( 2*n )
    (  n  )
    where n is the length of the grid
    """
    fact_n = factorial(length)
    return factorial(2*length)/(fact_n*fact_n)


if __name__ == "__main__":
    arg = int(sys.argv[1])

    def main():
        print lattice(arg)

    cProfile.run('main()')
