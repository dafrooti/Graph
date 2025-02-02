class Graph:
    def __init__(self, size):
        self.size = size
        self.graph = {}

        for i in range(self.size):
            self.graph[i] = []

    def BFS(self, source):
        result = []
        queue = []
        visited = [False]*self.size

        distance = [-1]*self.size

        queue.append(source)
        visited[source] = True
        distance[source] = 0

        while len(queue) > 0:
            temp = queue.pop(0)
            result.append(temp)

            for node in self.graph[temp]:
                if visited[node] == False:
                    queue.append(node)
                    visited[node] = True
                    distance[node] = distance[temp]+1
        #         print(visited)
        #         print(queue)
        # print(distance)
        return result

    def dfs_util(self, source, visited, result):
        result.append(source)
        visited[source] = True

        for node in self.graph[source]:
            if visited[node] == False:
                self.dfs_util(node, visited, result)
    
    def DFS(self, source):
        visited = [False]*self.size
        result = []
        self.dfs_util(source, visited, result)
        return result

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
    

graph = None

while True:
    print("Press 1 to create the graph")
    print("Press 2 to print BFS")
    print("Press 3 to print DFS")
    print("Press 4 to see if the graph is cyclic or not")
    print("Press 5 to exit")

    choice = int(input("Enter option: "))

    if choice == 1:
        amount = int(input("How many numbers would you like: "))
        graph = Graph(amount)
        for i in range(amount):
            x = int(input("What would you like the first number to be: "))
            y = int(input("What would you like the second number to be: "))
            graph.addedge(x, y)

    elif choice == 2:
        source = int(input("Which node would you like to start the search with: "))
        print(graph.BFS(source))

    elif choice == 3:
        source = int(input("Which node would you like to start the search with: "))
        print(graph.DFS(source))

    elif choice == 4:
        if graph.iscyclic():
            print("The graph has a cycle")
        else:
            print("The graph does not have a cycle")

    elif choice >= 5:
        break
    
    
# g1 = Graph(10)
# g1.addedge(1, 2)
# g1.addedge(2, 4)
# g1.addedge(4, 5)
# g1.addedge(8, 6)
# print(g1.graph)

# if g1.iscyclic():
#     print("The graph has a cycle")
# else:
#     print("The graph does not have a cycle")
