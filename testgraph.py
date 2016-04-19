# testgraph.py
import graphreader
import shortestpath

nodes, edges = graphreader.load_graph('testgraph1.txt')
assert shortestpath.shortest_path('O', 'T', nodes, edges)) == ['O', 'A', 'B', 'D', 'T']

