__author__ = "alestainer"

import scipy
import numpy as np
import math

def function(x):
	return math.sin(x) * x - math.cos(2 * x / 3 - 1) * x - math.exp(math.abs(x / 10))

def mutation_1(population, epsilon):
	best = get_best(population, 10)

	for i in best:
		for j in best:
			population.append((i + np.random.random(0, epsilon))
			 * (j + np.random.random(0, epsilon))
			 / ((i + np.random.random(0, epsilon)) + (j + np.random.random(0, epsilon))))

def selection_1(population, num, metric):
	return sorted(population, key = metric)[:num]

def metric_1(x):
	return 
