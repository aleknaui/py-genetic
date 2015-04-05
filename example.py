#!/usr/bin/env python
# -*- coding: utf-8 -*-
from genetic import *

# Example that maximizes the function (-(x-300)^2) + 200

def fitness(chromosome):
	x = Chromosome.decode(chromosome.chain) # Chromosome.chain is an array of 0 and 1 values
	return (((x-300)*-1)**2 + 200) / 10

p = Pool(10, 15, 0.7, 0.001, fitness) # arguments: chromosome_length, population_size, crossover_rate, mutation_rate, fitness_function
p.evolve(800) # argument: ammount of iterations
c = p.pick() # picks from the pool
max = Chromosome.decode(c.chain) # decodes the Chromosome

print max