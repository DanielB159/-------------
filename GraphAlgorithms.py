import networkx as nx
import matplotlib.pyplot as plt
from heapdict import heapdict



    
'''
SSSP - Single Source Shortest Path Algorithms. Ordered by:
- Belman Ford algorithm for directed/undirected weighed graphs with no negative cycles
- Dijkstra algorithm for directed/undirected weighed positive graphs
- BFS algorithm for directed/undirected unweighed graphs
'''


'''
The Relax function is used in relaxation based algorithms. Such as Dijkstra and Belman-Ford.
It recieves two vertices and function that returns the current distance for each vertex.
If the path from u to v is shorter than the current calculated path to v, change the
shortest path to v to be from u.
'''
def Relax(G, u, v, distFunction):
    distuv = G.nodes[u]["distance"] + G.edges[u, v]["weight"]
    print("u is:", u, "and v is", v)
    print("the current dist is", distFunction[v])
    if distuv < distFunction[v]:
        print("got here")
        # print("got here and the distance is:", distuv, "and the previous distance was:", distFunction[v])
        distFunction[v] = distuv
        print("now the dist is", distFunction[v] )
        # print("now the distance is:", distFunction[v])
        G.add_node(v, distance= G.nodes[u]["distance"] + G.edges[u, v]["weight"] ,pi = u)

'''
The Belman Ford algorithm solves the SSSP problem for a Weighed Directed / Undirected Graph.
The algorithm assumes that there are no negative cycles in the grapg.
'''
def Belman_Ford(G, source):
    distFunction = dict()
    # first, setting the weight of all nodes to be infinity
    for vertex in G.nodes:
        distFunction[vertex] = 2**30 # assumed to be infinity
    
    #next, setting all distances to be infinity, and all predecessors to be null
    for vertex in G.nodes:
        G.add_node(vertex, distance = 2**30, pi = None)
    
    # the source node will have distance zero from itself, and hightset priority
    distFunction[source] = 0
    G.add_node(source, distance = 0)
    # looping over all edges |V| - 1 times. As long as the longest possible path between two vertices
    for i in range(0, len(G.nodes()) + 1, 1): # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!DANIEL need to handle directed graph
        for (u,v) in G.edges():
            Relax(G, u, v, distFunction)
            Relax(G, v, u, distFunction) 
    
    for vertex in G.nodes:
        print(vertex, "distance: ", G.nodes[vertex]['distance'], "predecessor: ", G.nodes[vertex]['pi'])
    




'''
The Dijkstra algorithm solves the SSSP problem for a Weighed Directed / Undirected Graph.
The algorithm assumes that all edge weights are positive.
'''
def Dijkstra(G, source):
    minHeap = heapdict()
    # first, setting the weight of all nodes to be infinity
    for vertex in G.nodes:
        minHeap[vertex] = 2**30 # assumed to be infinity
    
    #next, setting all distances to be infinity, and all predecessors to be null
    for vertex in G.nodes:
        G.add_node(vertex, distance = 2**30, pi=None)
    
     # the source node will have distance zero from itself, and hightset priority
    minHeap[source] = 0
    G.add_node(source, distance = 0)
   
    # go over all of the nodes in the priority queue
    while len(minHeap) != 0:
        vertex = minHeap.popitem()[0]
        # print("the length of the heap is now:",len(minHeap))
        if G.nodes[vertex]["pi"] != None: # if the current node is not the source node
            # set the current vertex weight to add to the predecessors weight with the edge between them
            predecessor = G.nodes[vertex]["pi"]
            G.add_node(vertex, distance = G.nodes[predecessor]["distance"] + G.edges[predecessor, vertex]["weight"])
        
        # decrease Relax all of the neighbors of the vertex
        for neighbor in G[vertex]:
            if minHeap.get(neighbor) != None:
                Relax(G, vertex, neighbor, minHeap)


    for vertex in G.nodes:
        print(vertex, "distance: ", G.nodes[vertex]['distance'], "predecessor: ", G.nodes[vertex]['pi'])


'''
Breadth-First Search is an algorithm for scanning a graph.
It can be used here solve the SSSP problem in an Unweighed Directed / Undirected Graph.

'''
def BFS(G, source):
    queue = []
    # first, coloring all nodes in G to be white.
    for vertex in G.nodes:
        G.add_node(vertex, color = "white")
    #setting the current source distance from himself to be 0, and appending it to the queue.
    G.add_node(source, distance = 0, color = "black")
    queue.append(source)
    # this loop will continue while there are still nodes that have not been reacheds
    while(len(queue) != 0):
        vertex = queue.pop()
        for neighbor in G[vertex]:
            fatherDist = G.nodes[vertex]['distance']
            # if the current source has not been visited yet.
            if G.nodes[neighbor]['color'] == "white":
                G.add_node(neighbor, distance = fatherDist + 1, color = "black")
                queue.append(neighbor)
                
    for vertex in G.nodes():
        print(vertex, "distance: " , G.nodes[vertex]['distance'])


