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
            node_color=["green" if n in self.visited_nodes else "skyblue" for n in self.graph.nodes],
            edge_color="black"
        )
        self.canvas.draw()
        
    
    def animate_traversal(self, algo, start_node=0):
        if algo == "BFS":
            generator = alg.bfs(self.graph, start_node)
        elif algo == "DFS":
            generator = alg.dfs(self.graph, start_node)
        else:
            return
    
        def step():
            try:
                self.visited_nodes = next(generator)
                self.draw()
                self.root.after(1000, step) # Update every 1 second
            except StopIteration:
                pass
        step()

    

    def reset(self):
        self.visited_nodes = []
        self.draw()
