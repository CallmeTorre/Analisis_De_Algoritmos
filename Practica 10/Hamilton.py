# -*- coding: utf-8 -*-
"""
INSTITUTO POLITÉCNICO NACIONAL
ESCUELA SUPERIOR DE CÓMPUTO
Análisis de Algoritmos
GRUPO: 3CV1

ALUMNOS:
    Reyes Fragoso Roberto
    Torreblanca Faces Jesús Alexis

PROFESOR: Luna Benoso Benjamín

FECHA: 4/Diciembre/2017
"""

class Graph():

    def __init__(self, vertices):
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
        self.V = vertices

     # Checamos si el vertice es adyacente al vertice
     # agregado previamente y si no se encuentra en el
     # resultado.

    def isSafe(self, v, pos, path):
        # Checamos si el vertice y el ultimo vertice en el path son adyacentes.
        if self.graph[path[pos - 1]][v] == 0:
            return False

        # Checamos si el vertice no esta en el path.
        for vertex in path:
            if vertex == v:
                return False

        return True

    # Funcion revursiva de utilidad que nos ayuda a resolver el problema.
    def hamCycleUtil(self, path, pos):

        # Caso base: Si todos los vertices estan incluidos en path.
        if pos == self.V:
            # Ultimo vertice debe ser adyacente al primer vertice
            # en path para que sea un ciclo.
            if self.graph[path[pos - 1]][path[0]] == 1:
                return True
            else:
                return False

        # Prueba diferentes vertices como candidatos en el ciclo Hamiltoniano.
        # No probamos el 0 porque ya lo tomamos como punto de partida en hamCycle().
        for v in range(1, self.V):

            if self.isSafe(v, pos, path) == True:

                path[pos] = v

                if self.hamCycleUtil(path, pos + 1) == True:
                    return True

                # Removemos el vertice si no nos lleva a la solución
                path[pos] = -1

        return False

    def hamCycle(self):
        path = [-1] * self.V

        # Agregamos el 0 como primer vertice en path.
        # Si existe un ciclo Hamiltoniano entonces la solución
        # puede verse desde cualquier punto del ciclo por ser un grafo
        # no dirigido.
        path[0] = 0

        if self.hamCycleUtil(path, 1) == False:
            print "No existe la solución\n"
            return False

        self.printSolution(path)
        return True

    def printSolution(self, path):
        print "Existe la solución"
        for vertex in path:
            print vertex,
        print path[0], "\n"

def main():
    g1 = Graph(5)
    g1.graph = [[0, 1, 0, 1, 0],
                [1, 0, 1, 1, 1],
                [0, 1, 0, 0, 1],
                [1, 1, 0, 0, 1],
                [0, 1, 1, 1, 0], ]
    print("Grafo:")
    print("(0)---(1)---(2)")
    print(" |    / \    |")
    print(" |   /   \   |")
    print(" |  /     \  |")
    print("(3)---------(4)")
    g1.hamCycle()
    g2 = Graph(5)
    g2.graph = [[0, 1, 0, 1, 0],
                [1, 0, 1, 1, 1],
                [0, 1, 0, 0, 1],
                [1, 1, 0, 0, 0],
                [0, 1, 1, 0, 0], ]
    print("Grafo:")
    print("(0)---(1)---(2)")
    print(" |    / \    |")
    print(" |   /   \   |")
    print(" |  /     \  |")
    print("(3)         (4)")
    g2.hamCycle()
    g2.graph = [[0, 1, 0, 1, 0],
                [1, 0, 1, 1, 1],
                [0, 1, 0, 0, 1],
                [1, 0, 0, 0, 1],
                [0, 1, 0, 1, 0], ]
    print("Grafo:")
    print("(0)---(1)---(2)")
    print(" |           |")
    print(" |           |")
    print(" |           |")
    print("(3)---------(4)")
    g2.hamCycle()

if __name__ == '__main__':
    main()
