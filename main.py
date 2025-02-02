class Graph:
    def __init__(self, size):
        self.size = size
        self.graph = {}

        for i in range(self.size):
            self.graph[i] = []

    def addedge(self, x, y):
        self.graph[x].append(y)

    def cyclic(self, source, visited, recstack):
        visited[source] = True
        recstack[source] = True

        for neighbor in self.graph[source]:
            if visited[neighbor] == False:
                if self.cyclic(neighbor, visited, recstack):
                    return True
            elif recstack[neighbor] == True:
                return True
            
        recstack[source] = False
        return False

    def iscyclic(self):
        visited = [False]*self.size
        recstack = [False]*self.size
        for node in range(self.size):
            if not visited[node]:
                if self.cyclic(node, visited, recstack):
                    return True
        return False


g1 = Graph(10)
g1.addedge(1, 2)
g1.addedge(2, 4)
g1.addedge(4, 5)
g1.addedge(8, 6)
print(g1.graph)

if g1.iscyclic():
    print("The graph has a cycle")
else:
    print("The graph does not have a cycle")