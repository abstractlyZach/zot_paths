# testgraph.py
import graphreader
import shortestpath

import pprint

nodes, edges = graphreader.load_graph('testgraph1.txt')
assert shortestpath.shortest_path('O', 'T', nodes, edges) == ['O', 'A', 'B', 'D', 'T']

# example from "Algorithm Design and Applications" textbook pg. 402, 403
nodes, edges = graphreader.load_graph('airportgraph.txt')
pprint.pprint(shortestpath.find_shortest_paths('BWI', nodes, edges))
pprint.pprint(shortestpath.shortest_path('BWI', 'LAX', nodes, edges))

nodes, edges = graphreader.load_graph('campusgraph.txt')
pprint.pprint(shortestpath.shortest_path('RR20', 'RR12', nodes, edges))
