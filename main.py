import tkinter as tk
from tkinter import ttk
from graph_visualizer import GraphVisualizer
import networkx as nx

class GraphEditorApp():
    def __init__(self, root):
        self.root = root
        self.root.title("Graph Editor Tool")   

        # Create a saple graph 
        self.graph = nx.Graph()
        self.graph.add_edges_from([(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)])

        # Graph Visualizer Object
        self.visualizer = GraphVisualizer(self.root, self.graph)

        # Buttons
        controls  = ttk.Frame(self.root)
        controls.pack(pady=10)


        ttk.Button(controls, text="Run BFS", command=self.run_bfs).pack(side=tk.LEFT, padx=5)
        ttk.Button(controls, text="Run DFS", command=self.run_dfs).pack(side=tk.LEFT, padx=5)
        ttk.Button(controls, text="Run Reset", command=self.reset_graph).pack(side=tk.LEFT, padx=5)

    def run_bfs(self):
        self.visualizer.animate_traversal("BFS", start_node=0)

    def run_dfs(self):
        self.visualizer.animate_traversal("DFS", start_node=0)
    
    def reset_graph(self):
        self.visualizer.reset
    
if __name__ == "__main__":
    root = tk.TK()
    app = GraphEditorApp(root)
    root.mainloop()