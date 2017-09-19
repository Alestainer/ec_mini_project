__author__ = "alestainer"

import scipy
import numpy as np
import math

def geometric_mean(x, y):

	return ((x*y)/(x+y))

def objective_function(x):

	return np.sin(x) * x - np.cos(2 * x / 3 - 1) * x - np.exp(np.absolute(x / 10))

def mutation_1(population, epsilon):
	best = selection_1(population, 10, objective_function)

	for i in best:
		for j in best:
			population = np.append(population, (geometric_mean(i + np.random.normal(0, epsilon),
			 j + np.random.normal(0, epsilon))))

	return population

def selection_1(population, num, metric):
	
	new = np.argsort(objective_function(population))
	result = population[new][::-1]

	return result[:num], result[0], result[-1]


if __name__ == "__main__":
	
	population = np.linspace(-20, 20, num = 10)
	
	for i in range(10):

		population, _, _ = selection_1(population, 10, metric = objective_function)
		population = mutation_1(population, epsilon = 2.5)
	
	print (objective_function(selection_1(population, 1, objective_function)[0]))