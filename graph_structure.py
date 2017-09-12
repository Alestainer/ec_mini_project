__author__ = 'alestainer'

"""
Implementation of graph structure for voting modeling.
We use matrix representation to speed up calculations through vectorization, using numpy.
"""

import numpy as np


class Graph():

	def __init__(self, size, connectivity = 0.1):
		"""
		Size: the number of nodes
		connectivity: probability of connection between two nodes
		dims: number of issues to vote for.
		"""
		
		self.size = size

		matrix = np.zeros(shape = [size, size])
		for i in range(size ** 2):
			if i / size == i % size:
				matrix[i / size][i / size] = 0
			elif numpy.random.binomial(1, connectivity):
				matrix[i / size][i % size] = .5

		self.matrix = matrix

	def drop(self, index):
		self.matrix = np.delete(self.matrix, index, axis = 0)
		self.matrix = np.delete(self.matrix, index, axis = 1)