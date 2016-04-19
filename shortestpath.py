import priorityqueue
import numpy

def find_shortest_paths(start_node, nodes, edges):
	'''
	Takes in a graph and starting node and returns a dictionary that can be used to
	construct the shortest path to each other node.
	'''
	shortest_distances = dict()
	unvisited = priorityqueue.PriorityQueue()
	shortest_distances[start_node] = NodeInfo(0, None)
	for node in (nodes - {start_node}):
		shortest_distances[node] = NodeInfo(numpy.inf, None)
	for node in nodes:
		# print(type(shortest_distances[node].previous_weight))
		# print(shortest_distances[node].previous_weight)
		#
		unvisited.add(node, shortest_distances[node].previous_weight)
	while not unvisited.is_empty():
		current_node = unvisited.pop()
		for unvisited_node in (unvisited.keys() & adjacent(current_node, edges)):
			new_distance = shortest_distances[current_node].previous_weight + get_weight(current_node, unvisited_node, edges)
			if new_distance < shortest_distances[unvisited_node].previous_weight:
				shortest_distances[unvisited_node].previous_weight = new_distance
				shortest_distances[unvisited_node].previous_node = current_node
				unvisited.add(unvisited_node, shortest_distances[unvisited_node].previous_weight)
	return shortest_distances


def shortest_path(start_node, end_node, nodes, edges):
	'''
	Takes in a graph, start node, end node, and returns a list of the
	nodes in order from the start node to the end node along the shortest path
	'''
	paths = find_shortest_paths(start_node, nodes, edges)
	answer = []
	current_node = end_node
	current_node_info = paths[current_node]
	while current_node_info.previous_node != None:
		answer.insert(0, current_node)
		current_node = paths[current_node].previous_node
		current_node_info = paths[current_node]
	answer.insert(0, current_node)
	if len(answer) == 1:
		return None
	return answer


def get_weight(node1, node2, edges):
	'''
	Takes in two nodes and a dictionary of edges, then returns the weight of the edge directly
	connecting them. Raises an EdgeNotFoundError if the edge doesn't exist.
	'''
	try:
		return edges[(node1, node2)]
	except KeyError:
		try:
			return edges[(node2, node1)]
		except KeyError:
			pass
	raise EdgeNotFoundError(node1, node2) 


def adjacent(node, edges):
	to_return = set()
	for node1, node2 in edges.keys():
		if node1 == node:
			to_return.add(node2)
		elif node2 == node:
			to_return.add(node1)
		else:
			pass
	return to_return


class NodeInfo:
	def __init__(self, previous_weight, previous_node):
		self.previous_weight = previous_weight
		self.previous_node = previous_node

	def __str__(self):
		return '({}, {})'.format(self.previous_weight, self.previous_node)

	def __repr__(self):
		return self.__str__()


class EdgeNotFoundError(Exception):
	def __init__(self, *args, **kwargs):
		Exception.__init__(self, *args, **kwargs)

