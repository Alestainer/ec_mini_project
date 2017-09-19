__author__ = "alestainer"

import scipy
import numpy as np
import math

def geometric_mean(x, y):

	return ((x*y)/(x+y))

def function(x):

	return np.sin(x) * x - np.cos(2 * x / 3 - 1) * x - np.exp(np.absolute(x / 10))

def mutation_1(population, epsilon):
	best = selection_1(population, 10, metric_1)

	for i in best:
		for j in best:
			population = np.append(population, (geometric_mean(i + np.random.normal(0, epsilon),
			 j + np.random.normal(0, epsilon))))

	return population

def selection_1(population, num, metric):
	
	new = np.argsort(metric_1(population))
	result = population[new][::-1]

	return result[:num]

def metric_1(x):

	return function(x)




if __name__ == "__main__":
	
	population = np.linspace(-20, 20, num = 10)
	
	for i in range(10):

		population = selection_1(population, 10, metric = metric_1)
		population = mutation_1(population, epsilon = 0.5)
	
	print (metric_1(selection_1(population, 1, metric_1)))
