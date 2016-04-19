# graphreader.py
import pprint

def load_graph(file_name):
	edges = dict()
	with open(file_name, 'r') as graph_file:
		current_line = graph_file.readline()
		nodes = set(current_line.strip().split(' '))
		for line in graph_file.readlines():
			node1, node2, weight = line.strip().split(' ')
			edges[(node1, node2)] = int(weight)
	return nodes, edges