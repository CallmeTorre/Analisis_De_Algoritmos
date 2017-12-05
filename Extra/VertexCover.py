def vertexCover(graph):
    solution = []
    size = len(graph)
    visited = [None for elem in range(size)]

    for i in range(size):
        if(visited[i] == None):
            lista = graph[i]
            for elem in lista:
                print("iteracion %d elem %d" %(i,elem))
                visited[i] = True
                visited[elem] = True
                if(i not in solution):
                    solution.append(i)
    print(solution)

a = {0:[1,2],
 1:[0],
 2:[0,3],
 3:[1,2]}
b = {0:[1,2],
  1:[0,3],
  2:[0],
  3:[1,4],
  4:[3,5],
  5:[4,6],
  6:[5]}
c = {0:[1],
    1:[0,2],
    2:[1,3,4],
    3:[2,5],
    4:[2,5,6],
    5:[3,4],
    6:[4]}
print("Grafo:")
print("(0)---------(1)")
print(" |           |")
print(" |           |")
print(" |           |")
print("(2)---------(3)")
vertexCover(a)
print("Grafo:")
print("(0)---------(2)")
print(" | ")
print(" | ")
print("(1)---------(3)")
print("             |")
print("             |")
print("(5)---------(4)")
print(" | ")
print(" | ")
print("(6)")
vertexCover(b)
print("(1)---------(2)---------(4)---------(6)")
print(" |           |           |")
print(" |           |           |")
print(" |           |           |")
print("(0)         (3)---------(5)")
vertexCover(c)
