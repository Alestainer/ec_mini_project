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
	

	def drop_vertex(self, index):
		
		self.matrix = np.delete(self.matrix, index, axis = 0)
		self.matrix = np.delete(self.matrix, index, axis = 1)
		self.size -= 1


	def add_vertex(self):
		
		vector = np.random.binomial(1, connectivity, self.size) * .5
		vector_2 = np.append(vector, [0])
		
		self.matrix = np.vstack((self.matrix, vector))
		self.matrix = np.column_stack((self.matrix, vector_2))
