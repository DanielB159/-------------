import networkx as nx
import matplotlib.pyplot as plt
from heapdict import heapdict


'''
The Relax function is used in relaxation based algorithms. Such as Dijkstra and Belman-Ford.
It recieves two vertices and function that returns the current distance for each vertex.
If the path from u to v is shorter than the current calculated path to v, change the
shortest path to v to be from u.
'''
def Relax(G, u, v, distFunction):
    distuv = G.nodes[u]["distance"] + G.edges[u, v]["weight"]
    if distuv < distFunction[v]:
        distFunction[v] = distuv
        G.add_node(v, pi=u)
    

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
