from collections import defaultdict 
import networkx as nx
import matplotlib.pyplot as plt
import re

graph = defaultdict(list)
#here is the word to be checked 
word = "baababaabb"
s = """VN={S, A, B, C},
        VT={a, b},P={ 1. S ->bA     2. A ->b    3. A ->aB   4. B ->bC    5. C ->cA 6. A ->bA 7. B ->aB }"""
def addEdge(graph,u,v): 
    graph[u].append(v) 

def generate_edges(graph): 
    edges = [] 
    for node in graph: 
        for neighbour in graph[node]: 
            edges.append((node, neighbour)) 
    return edges 
  
def parseString(str):
    str = str.split()
    str = "".join(str).split("P={")[1]
    if str[-1] == '}':
        str = str[:-1]
    str = re.split("\d+\.", str)
    return list(filter(len, str))

def checkAutomaton(graph, source, word):
    for neighbour in graph[source]:
        for key in neighbour:
            if neighbour[key] == word[0]:
                # print(source + " -> " + key + " prin " + neighbour[key] +  " word " + word)  
                word = word[1:]
                if len(word) == 0 and key == "None":
                    return True
                else:
                    if len(word) == 0 or key == "None":
                        return False
                return checkAutomaton(graph, key, word)
    return False

def addToGraph(list):
    for i in list:
        temp = i.split("->")
        currentGraph =temp[0]
        pointTo = temp[1]
        if len(pointTo) < 2:
            addEdge(graph, currentGraph, {'None': pointTo[0]})
        else:
            addEdge(graph, currentGraph, {pointTo[1]: pointTo[0]})

def draw():  
    g = nx.DiGraph()
    for k, v in graph.items():
        for vv in v:
            for t in vv:
                g.add_edge(k,t) 
    nx.draw(g,with_labels=True)
    plt.draw()
    plt.show()

addToGraph(parseString(s))
print(checkAutomaton(graph, 'S', word))

draw()


