from enum import Enum
from typing import Any, Optional, Dict, List
import copy
import sys
sys.path.append('c:\\Users\\adria\\Desktop\\Programming\Python')
from Lab_02 import *


class EdgeType(Enum):
    directed = 1
    undirected = 2


class Vertex:
    data: Any
    index: int

    def __init__(self,data,ind):
        self.data=data
        self.index=ind

    def __repr__(self):
        return f'{self.data}:v{self.index}'


class Edge:
    source: Vertex
    destination: Vertex
    weight: Optional[float]

    def __init__(self,s,d,w):
        self.source=s
        self.destination=d
        self.weight=w

    def __repr__(self):
        return f'{self.destination}'


class Graph:
    adjacencies: Dict[Vertex, List[Edge]]

    def __init__(self):
        self.adjacencies= dict()

    def create_vertex(self, data: Any):
        self.adjacencies[Vertex(data,len(self.adjacencies))]=list()

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None):
        grafik.adjacencies[source].append(Edge(source,destination,weight))

    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None):
        grafik.adjacencies[source].append(Edge(source,destination,weight))
        grafik.adjacencies[destination].append(Edge(destination,source,weight))

    def add(self, edge: EdgeType, source: Vertex, destination: Vertex, weight: Optional[float] = None):
        if edge.name=="directed":
            self.add_directed_edge(source,destination,weight)
        else:
            self.add_undirected_edge(source,destination,weight)

    def traverse_breadth_first(self, visit):
        lista_kluczy=[]
        lista_odwiedzonych=[]
        for x in self.adjacencies.keys():
            lista_kluczy.append(x)
        kolejka= Lab_02_pd.Queue()
        kolejka.enqueue(lista_kluczy[0])
        while(len(kolejka)!=0):
            new=kolejka.dequeue()
            lista_odwiedzonych.append(new)
            visit(new)
            for new_neighbour in self.adjacencies[new]:
                if new_neighbour.destination in lista_odwiedzonych:
                    True
                else:
                    kolejka.enqueue(new_neighbour.destination)

    def traverse_depth_first(self, visit):
        lista_kluczy=[]
        lista_odwiedzonych=[]
        for x in self.adjacencies.keys():
            lista_kluczy.append(x)
        v_new=lista_kluczy[0]
        self._dfs(v_new, lista_odwiedzonych, visit)

    def _dfs(self,v: Vertex, visited: List[Vertex], visit):
        visit(v)
        visited.append(v)
        for new_neighbour in self.adjacencies[v]:
                if new_neighbour.destination in visited:
                    True
                else:
                    self._dfs(new_neighbour.destination,visited,visit)

    def show(self):
        True #TODO
        
    def __repr__(self):
        stirng = ""
        for data in self.adjacencies:
            stirng+=f'- {data} ---->{self.adjacencies[data]}\n'
        return stirng
          
        

grafik = Graph()
grafik.create_vertex(0)
grafik.create_vertex(1)
grafik.create_vertex(2)
grafik.create_vertex(3)
grafik.create_vertex(4)
grafik.create_vertex(5)
lista=grafik.adjacencies.keys()
lista_kluczy=[]
for x in lista:
    lista_kluczy.append(x)
grafik.add(EdgeType(1),lista_kluczy[0],lista_kluczy[1])
grafik.add(EdgeType(1),lista_kluczy[0],lista_kluczy[5])
grafik.add(EdgeType(1),lista_kluczy[5],lista_kluczy[1])
grafik.add(EdgeType(1),lista_kluczy[5],lista_kluczy[2])
grafik.add(EdgeType(1),lista_kluczy[2],lista_kluczy[2])
grafik.add(EdgeType(1),lista_kluczy[2],lista_kluczy[3])
grafik.add(EdgeType(1),lista_kluczy[3],lista_kluczy[4])
grafik.add(EdgeType(1),lista_kluczy[4],lista_kluczy[1])
grafik.add(EdgeType(1),lista_kluczy[4],lista_kluczy[5])
print(grafik.adjacencies)
grafik.traverse_breadth_first(print)
print()
grafik.traverse_depth_first(print)
#print(grafik.adjacencies[lista_kluczy[0]][0].destination.data)
print(grafik)
