import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import graph_algorithms as alg
import tkinter as tk

class GraphVisualizer:
    def __init__(self, root, graph):
        self.root = root
        self.graph = graph 
        self.pos = nx.spring_layout(graph)
        self.visited_nodes = []

        