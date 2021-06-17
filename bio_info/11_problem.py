def StringReconstruction(Patterns):
    dB = DeBruijn(Patterns)
    path = EulerianPath(dB)
    text = PathToGenome(path)
    return text

def DeBruijn(Patterns):
    k, data = int(Patterns[0]), Patterns[1:]
    graph = {}
    for string in data:
        if (not graph.get(string[:k-1])):
            graph[string[:k-1]]=[]
        if (not graph.get(string[1:])):
            graph[string[1:]]=[]
        graph[string[:k - 1]].append(string[1:])
    return graph

def get_balance(graph):
    balance = {}
    for key in graph:
        balance[key] = 0
    for key in graph:
        for out in graph[key]:
            balance[key] -= 1
            balance[out] += 1

    return balance

def EulerianPath(graph):
    balance = get_balance(graph)
    answ = []
    stack = []
    for u in balance:
        if balance[u] == -1:
            v = u
    stack.append(v)
    while (stack !=[]):
        w = stack[-1]
        if (graph[w]==[]):
            answ.append(stack.pop())
        else:
            for u in graph[w]:
                stack.append(u)
                graph[w].remove(u)
                found_edge = True
                break;
            if not found_edge:
                answ.append(stack.pop())
    return answ

def PathToGenome(path):
    path = path[::-1]
    answ = path[0]
    for i in path[1:]:
        answ+=i[len(i)-1]

    return answ



data = "".join(open('StringReconstructionProblem.txt')).split()
print(StringReconstruction(data))