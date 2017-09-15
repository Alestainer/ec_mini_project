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

		self.matrix = np.random.binomial(1, connectivity, size = (size, size))
		self.matrix = np.fill_diagonal(self.matrix, 0)
	
	def drop_vertex(self, indices):
		"""
		Drop vertices from the matrix by index.
		"""
		self.matrix = np.delete(self.matrix, indices, axis = 0)
		self.matrix = np.delete(self.matrix, indices, axis = 1)
		self.size -= len(indices)

	def add_vertex(self, connectivity):
		"""
		Add vertex in the end of matrix, initialized with new connectivity.
		"""
		vector = np.random.binomial(1, connectivity, self.size) * .5
		vector_2 = np.append(vector, [0])
		
		self.matrix = np.vstack((self.matrix, vector))
		self.matrix = np.column_stack((self.matrix, vector_2))
		self.size += 1

	def add_vertices(self, num, connectivity):
		"""
		Add multiple vertices.
		"""
		for i in range(num):
			self.add_vertex(connectivity)

	def calculate_value(self):
		"""
		Calculate sum of connections for the vertices.
		"""
		return np.sum(self.matrix, axis = 1)
