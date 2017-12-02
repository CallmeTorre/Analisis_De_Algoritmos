def vertexCover(graph):
    solution = []
    size = len(graph)
    visited = [None for elem in range(size)]

    for i in range(size):
        if(visited[i] == None):
            lista = graph[i]
            for j,elem in enumerate(lista):
                if nextElem(j,len(lista)) == None:
                    break
                siguiente = lista[j+1]
                if(visited[siguiente] == None):
                    print("iteracion %d elem %d" %(i,elem))
                    visited[i] = True
                    visited[elem] = True
                    if(i not in solution):
                        solution.append(i)
    print(solution)

def nextElem(index,lenArray):
    if index+1 == lenArray:
        return None
    return True
#a = {0:[1,2],
# 1:[0],
# 2:[0,3],
# 3:[2]}
#a = {0:[1,2],
#  1:[0,3],
#  2:[0],
#  3:[1,4],
#  4:[3,5],
#  5:[4,6],
#  6:[5]}
#a = {0:[1],
#    1:[0,2],
#    2:[1,3,4],
#    3:[2,4,5],
#    4:[2,3,5,6],
#    5:[3,4],
#    6:[4]}
vertexCover(a)
