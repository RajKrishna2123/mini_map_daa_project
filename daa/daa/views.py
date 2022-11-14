
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return  render(request ,"index.html")
def ABOUT(request):
    return  render(request ,"login.html")
def DATASAVE(request):  
    return  render(request ,"login3.html")
def ADDITION(request):   
    start=request.GET.get('stan','default')    
    end=request.GET.get('ap_by','default')
    p=int(start)
    import sys
    from queue import PriorityQueue
    class Graph:
        def __init__(self, num_of_vertices):
            self.v = num_of_vertices
            self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
            self.visited = []
        def add_edge(self, u, v, weight):
            self.edges[u][v] = weight
            self.edges[v][u] = weight
    def dijkstra(graph, start_vertex):
        D = {v:float('inf') for v in range(graph.v)}
        D[start_vertex] = 0

        pq = PriorityQueue()
        pq.put((0, start_vertex))

        while not pq.empty():
            (dist, current_vertex) = pq.get()
            graph.visited.append(current_vertex)

            for neighbor in range(graph.v):
                if graph.edges[current_vertex][neighbor] != -1:
                    distance = graph.edges[current_vertex][neighbor]
                    if neighbor not in graph.visited:
                        old_cost = D[neighbor]
                        new_cost = D[current_vertex] + distance
                        if new_cost < old_cost:
                            pq.put((new_cost, neighbor))
                            D[neighbor] = new_cost
        return D
    g = Graph(9)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 6, 7)
    g.add_edge(1, 6, 11)
    g.add_edge(1, 7, 20)
    g.add_edge(1, 2, 9)
    g.add_edge(2, 3, 6)
    g.add_edge(2, 4, 2)
    g.add_edge(3, 4, 10)
    g.add_edge(3, 5, 5)
    g.add_edge(4, 5, 15)
    g.add_edge(4, 7, 1)
    g.add_edge(4, 8, 5)
    g.add_edge(5, 8, 12)
    g.add_edge(6, 7, 1)
    g.add_edge(7, 8, 3)
    D = dijkstra(g, p)
    dict={'0':'Jd women’s college','1':'Dav public school','2':'B.D.P school','3':'Study centre','4':'ICFAUI university','5':'Kurukshetra University','6':'International school','7':'Bal Bharti public school','8':'Indian public school','9':'RKD college'}
    print(D)
    v=[]
    for vertex in range(len(D)):
        v.append(vertex)
        print("Distance from start ",dict[start]," to destination", dict[str(vertex)], "is",        D[vertex])
    return render (request,"contactconfirmation.html")
            
def description(request):
    return  render(request,"contactconfirmation2.html")
