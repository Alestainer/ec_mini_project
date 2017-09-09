__author__ = 'alestainer'
"""Evolution of agents in an environment.
Environment, agent strategies, mutation and selection operators may vary significantly."""


class Evolution():
	
	def __init__(self,
	 env,
	 metric,
	 num_species,
	 specie,
	 mutation_operator,
	 selection_operator,
	 num_steps = None):
		
		self.env = env
		self.metric = metric
		self.num_species = num_species
		self.specie = specie
		self.mutation_operator = mutation_operator
		self.selection_operator = selection_operator
		self.num_steps = num_steps

		self.step = 0
		self.population = self.random_select(num_species, specie)


# Run one step of mutation


# Run one step of selection


# Work the evolution process
	def work(self):

		while self.step < self.num_steps:
			
			self.mutate()
			self.select()

			if self.step % 1000 = 0:
				print ("Step #" + str(self.step))



# Show the best population


