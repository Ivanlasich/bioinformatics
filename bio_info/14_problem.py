class Point:
    def __init__(self, ent, out):
        self.ent = ent
        self.out = out

def MaximalNonBranchingPaths(Graph):
    Paths = []
    balance = get_balanced(Graph)
    for v in Graph:
        if (balance[v] != [1, 1]):
            if (balance[v][0] > 0):
                for w in Graph[v]:
                    NonBranchingPath = v
                    NonBranchingPath += w[-1]
                    while balance[w]==[1, 1]:
                        w = Graph[w][0]
                        NonBranchingPath += w[-1]
                    Paths.append(NonBranchingPath)

    return Paths


def DeBruijn(k, Patterns):
    graph = {}
    for string in Patterns:
        if (not graph.get(string[:k-1])):
            graph[string[:k-1]]=[]
        if (not graph.get(string[1:])):
            graph[string[1:]]=[]
        graph[string[:k - 1]].append(string[1:])
    return graph

def get_balance(graph):
    balance = {}
    for key in graph:
        balance[key] = Point(0, 0)
    for key in graph:
        for out in graph[key]:
            balance[key].out += 1
            balance[out].ent += 1

    return balance

def get_balanced(graph):
    balance = {}
    for key in graph:
        balance[key] = [0, 0]
    for key in graph:
        for out in graph[key]:
            balance[key][0] += 1
            balance[out][1] += 1

    return balance

data = "".join(open('StringReconstructionProblem.txt')).split()
k = len(data[0])
answ = DeBruijn(k, data)
print(' '.join(sorted(MaximalNonBranchingPaths(answ))))