
def StringReconstruction(k):
    Patterns = vector_generation(k)
    dB = DeBruijn(k, Patterns)
    path = EulerianPath(dB)
    text = PathToGenome(k, path)
    return text

def DeBruijn(k, Patterns):
    graph = {}
    for string in Patterns:
        if (not graph.get(string[:k-1])):
            graph[string[:k-1]]=[]
        if (not graph.get(string[1:])):
            graph[string[1:]]=[]
        graph[string[:k - 1]].append(string[1:])
    return graph

def EulerianPath(graph):
    answ = []
    stack = []
    for v in graph:
        break;

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

def PathToGenome(k, path):
    path = path[(k - 1):]
    path = path[::-1]
    answ = path[0]
    for i in path[1:]:
        answ+=i[len(i)-1]

    return answ


def construct(vec, k):
    answ =''
    vec = vec[2:]
    n = k - len(vec)
    for i in range(n):
        answ+='0'
    return answ+vec

def vector_generation(k):
    answ = []
    for i in range(2**k):
        answ.append(construct(bin(i), k))
    return answ




print(StringReconstruction(8))
print(len(StringReconstruction(8)))
