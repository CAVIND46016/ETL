import os

import pandas as pd
import pydot


os.environ["PATH"] += os.pathsep + "C:/Program Files (x86)/Graphviz2.38/bin/"

filename = "pydot.png"
graph = pydot.Dot(graph_type="digraph")

apex_level = "root"

for i in range(3):
    edge = pydot.Edge(apex_level, "level {}".format(i + 1))
    graph.add_edge(edge)

for i in range(3):
    for j in range(3):
        edge = pydot.Edge("level {}".format(i + 1), "sublevel {}".format(j + 1))
        graph.add_edge(edge)


graph.write_png(filename)
print("Completed")
# Opens the file using the default windows program associated with the image
os.startfile(filename, "open")
