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

        # Create matplotlib figure
        self.fig, self.ax = plt.subplots(figsize=(5,4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack()

        self.reset()

    
    def draw(self):
        self.ax.clear()
        nx.draw(
            self.graph, self.pos, ax=self.ax,
            with_labels=True,
            node_color=["green" if n in self.visited_nodes else "skyblue" for n in self.grpah.nodes],
            edge_color="black"
        )
        self.canvas.draw()
        