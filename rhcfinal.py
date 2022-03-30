# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 21:34:46 2022

@author: taile
"""

from numpy import asarray
from numpy import exp
from numpy import sqrt
from numpy import cos
from numpy import e
from numpy import pi
from numpy import sin
from numpy.random import randn
from numpy.random import rand
from numpy.random import seed
import enum

class position(enum.Enum):
    x = 0
    y = 0

#objective function
def func(x, y):
    phold = y+47 #placeholder so isn't as messy
    return -(phold) + sin(sqrt(abs((x/2)+(phold)))) - (x * sin(sqrt(abs(x-phold))))


# check if a point is within the bounds of the search
def in_bounds(point, bounds):
	# enumerate all dimensions of the point
	for d in range(len(bounds)):
		# check if out of bounds for this dimension
		if point[d] < bounds[d, 0] or point[d] > bounds[d, 1]:
			return False
	return True

# hill climbing local search algorithm
def hillclimbing(func, bounds, n_iterations, step_size, start_pt):
	# store the initial point
	solution = start_pt
	# evaluate the initial point
	solution_eval = func(404,504)
	# run the hill climb
	for i in range(n_iterations):
		# take a step
		candidate = None
		while candidate is None or not in_bounds(candidate, bounds):
			candidate = solution + randn(len(bounds)) * step_size
		# evaluate candidate point
		candidte_eval = func(404,504)
		# check if we should keep the new point
		if candidte_eval <= solution_eval:
			# store the new point
			solution, solution_eval = candidate, candidte_eval
	return [solution, solution_eval]

# hill climbing with random restarts algorithm
def random_restarts(func, bounds, n_iter, step_size, n_restarts):
	best, best_eval = None, 1e+10
	# enumerate restarts
	for n in range(n_restarts):
		# generate a random initial point for the search
		start_pt = None
		while start_pt is None or not in_bounds(start_pt, bounds):
			start_pt = bounds[:, 0] + rand(len(bounds)) * (bounds[:, 1] - bounds[:, 0])
		# perform a stochastic hill climbing search
		solution, solution_eval = hillclimbing(func, bounds, n_iter, step_size, start_pt)
		# check for new best
		if solution_eval < best_eval:
			best, best_eval = solution, solution_eval
			print('Restart %d, best: f(%s) = %.5f' % (n, best, best_eval))
	return [best, best_eval]

# seed the pseudorandom number generator
seed(2)
# define range for input
bounds = asarray([[-3.0, 3.0], [-3.0, 3.0]])
# define the total iterations
n_iter = 23
# define the maximum step size
step_size = 0.05
# total number of random restarts
n_restarts = 30
# perform the hill climbing search
best, score = random_restarts(func, bounds, n_iter, step_size, n_restarts)
print('Done!')
print('f(%s) = %f' % (best, score))