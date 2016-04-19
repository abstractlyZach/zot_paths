# adapted from python 3.5 documentation
# https://docs.python.org/3.5/library/heapq.html

import itertools
import heapq


REMOVED = '<removed-item>'      # placeholder for a removed item


class PriorityQueue:
	def __init__(self):
		self._pq = []                         # list of entries arranged in a heap
		self._entry_finder = {}               # mapping of items to entries
		self._counter = itertools.count()     # unique sequence count

	def add(self, item, priority=0):
		'Add a new item or update the priority of an existing item'
		if item in self._entry_finder:
			self._remove(item)
		count = next(self._counter)
		entry = [priority, count, item]
		self._entry_finder[item] = entry
		heapq.heappush(self._pq, entry)

	def _remove(self, item):
		'Mark an existing item as REMOVED.  Raise KeyError if not found.'
		entry = self._entry_finder.pop(item)
		entry[-1] = REMOVED

	def pop(self):
		'Remove and return the lowest priority item. Raise KeyError if empty.'
		while self._pq:
			priority, count, item = heapq.heappop(self._pq)
			if item is not REMOVED:
				del self._entry_finder[item]
				return item
		raise KeyError('pop from an empty priority queue')

	def is_empty(self):
		'Returns True if the priority queue is empty, False otherwise.'
		return len(self._entry_finder) == 0

	def contains(self, item):
		'''
		Returns true if the node is in the priority queue.
		'''
		return item in self._entry_finder

	def keys(self):
		return set(self._entry_finder.keys())
		