from sys import maxsize
def BellmanFordAlg(xx, Nodes, Edges, src):
    edge = [maxsize] * Nodes
    edge[src] = 0
    for i in range(Nodes - 1):
        for j in range(Edges):
            if edge[xx[j][0]] + \
                   xx[j][2] < edge[xx[j][1]]:
                edge[xx[j][1]] = edge[xx[j][0]] + \
                                       xx[j][2]
    for i in range(Edges):
        x = xx[i][0]
        y = xx[i][1]
        weight = xx[i][2]

        if edge[x] != maxsize and edge[x] + \
                        weight < edge[y]:

            print("Error")


    print("Node/Vertex : Optimal distance")
    for i in range(Nodes):
        print("%d:%d" % (i, edge[i]))
 
if __name__ == "__main__":
    Nodes = 7
    Edges = 10
    xx = [[0, 1, 6], [0, 2, 5], [0, 3, 5], [1, 4, -1], [2, 1, -2], [2, 4, 1], [3, 2, -2], [3, 5, -1], [4,6,3], [5,6,3]]
    BellmanFordAlg(xx, Nodes, Edges, 0)
 
# This code is contributed by
# sanjeeNodes2552