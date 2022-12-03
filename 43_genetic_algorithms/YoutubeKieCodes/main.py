# https://www.youtube.com/watch?v=nhT56blfRpE
from random import choices, randint, randrange, random
from typing import List, Dict, Callable, Tuple
import logging
from collections import namedtuple
from functools import partial

logging.basicConfig(
	filename = 'info.log',
	filemode = 'w',
	level = logging.INFO)
log = logging.getLogger(__name__)

Genome = List[int]
Population = List[Genome]
FitnessFunc = Callable[[Genome], int]
PopulateFunc = Callable[[], Population]
SelectionFunc = Callable[[Population, FitnessFunc], Tuple[Genome, Genome]]
CrossoverFunc = Callable[[Genome, Genome], Tuple[Genome, Genome]]
MutationFunc = Callable[[Genome], Genome]
Thing = namedtuple(
	'Thing',
	['name','value','weight']
)

def generate_genome(length: int) -> Genome:
	'''
	Generates the genome sequence, that is, sequence of binary numbers which corresponds to existing
	or not a object from the thing struct
	'''
	return choices([0,1], k=length) 

def generate_population(size: int, genome_length: int) -> Population:
	'''
	Generates a population of genomes
	'''
	return [generate_genome(genome_length) for _ in range(size)]

def fitness(genome: Genome, things: List[Thing], weight_limit: int) -> int:
	'''
	Returns the value of points of a given thing, that is, corresponding to a given genome.
	It will return 0, if the weight exceeds the pre-definied limit, that is, meaning that the passed genome does not satisfy the condition
	the problem's bound
	'''
	if len(genome) != len(things):
		raise ValueError("genome and things must be of the same length")

	weight = 0
	value = 0

	for genome_index, thing in enumerate(things):
		if genome[genome_index] == 1:
			'''
			Selects this element, so, when element is present, the weight and value are calculated
			Throughout iterations, as they proceed, the element which is present, and keeps appearing in different genomes,
			will be selected for newer generations, as it survived, not exceeding the weight limit
			'''
			log.debug(f'The object {thing} is present')
			
			weight += thing.weight
			value += thing.value
			
			if weight > weight_limit:
				return 0
	
	return value

def selection_pair(population: Population, fitness_func:FitnessFunc, things:Thing) -> Population:
	'''
	Returns a pair of genomes, from the input of genomes
	It chooses, in general, more "good" genomes, which received higher scores according to the fitness function
	
	'''
	natural_selected_population = choices(
		population=population,
		weights=[fitness_func(genome) for genome in population],
		k=2
		)
	
	natural_selected_population_things = [genome_to_things(genome, things) for genome in natural_selected_population]
	fitness_values = [fitness_func(genome) for genome in natural_selected_population]
	log.debug(f'''
	Survived best population are: {natural_selected_population_things}
	and 
	Fitness value are {fitness_values}
	''')

	return natural_selected_population


def single_point_crossover(a: Genome, b: Genome) -> Tuple[Genome, Genome]:
	'''
	Returns the genomes after the crossover, was applied to both genomes, that is, the exchange of things between genomes
	'''
	if len(a) != len(b):
		raise ValueError("Genomes a and b must be the same length")
	
	length = len(a)
	if length < 2:
		return a, b

	p = randint(1, length -1)

	a_cross = a[:p] + b[p:]
	b_cross = b[:p] + a[p:]

	return a_cross, b_cross

def mutation(genome: Genome, num:int = 1, probability:float = 0.5) -> Genome:
	'''
	Bit flips randomly a Genome

	-------------------------------------
	Parameters:
	num: Number of mutations
	'''

	for _ in range(num):
		# Randomly bringing up a index to apply the mutation	
		index = randrange(len(genome))
		# applying the mutation, if probability a random value generated is bigger than the default probability passed as argument
		# if the random number generated is not greater than probability, returns 0 or 1, according to the value presented in genome[index]
		genome[index] = genome[index] if random() > probability else abs(genome[index] -1)

	return genome


def genome_to_things(genome:Genome, things: List[Thing]) -> List[Thing]:
	'''
	Maps genome to the thing
	'''
	result = []
	for genome_index, thing in enumerate(things):
		if genome[genome_index] == 1:
			result += [thing.name]

	return result
		

def run_evolution(
	populate_func: PopulateFunc,
	fitness_func: FitnessFunc,
	fitness_limit: int,
	things:Thing,
	selection_func: SelectionFunc = selection_pair,
	crossover_func: CrossoverFunc = single_point_crossover,
	mutation_func: MutationFunc = mutation,
	generation_limit: int = 100
	) -> Tuple[Population, int]:
	
	population = populate_func()
	
	for generation in range(generation_limit):
		population = sorted(
			population,
			#according to each objective result value from the individual population genome, sort the population
			key = lambda genome: fitness_func(genome),
			reverse = True
		)

		if fitness_func(population[0]) >= fitness_limit:
			break
		
		# next generation will receive only the best selected by fitness_func, as it was sorted
		next_generation = population[0:2]
		
		# Loop through half the lenght of the population to 
		for _ in range(int(len(population)/2) -1):
			'''
			New genomes will be selected, according to the input population and fitness_func we are using
			I will think that as input data, off course, and objective function
			'''
			# randomly chooses two genomes to survive
			parents = selection_func(
				population = population, 
				fitness_func = fitness_func, 
				things = things)
			
			# applies the crossover to those two genomes
			offspring_a, offspring_b = crossover_func(parents[0], parents[1])
			
			# apply the mutation function to each offspring
			offspring_a = mutation_func(offspring_a)
			offspring_b = mutation_func(offspring_b)

			next_generation += [offspring_a, offspring_b]

			natural_selected_population_things = [genome_to_things(genome, things) for genome in next_generation]
			fitness_values = [fitness_func(genome) for genome in next_generation]
			log.info(f'''
			Generation {generation} Survived best genomes are: {list(zip(natural_selected_population_things,fitness_values))}
			''')
		
		population = next_generation


			

	population = sorted(
		 population,
		 key = lambda genome: fitness_func(genome),
		 reverse=True 
	)

	return population, generation





if __name__ == '__main__':

	THINGS = [
	Thing('Laptop', 500, 2200),
	Thing('Headphones', 150, 160),
	Thing('Coffee Mug', 60, 350),
	Thing('Notepad', 40, 333),
	Thing('Water Bottle', 30, 192)
	]

	MORE_THINGS = [
	Thing('Mints', 5, 25), 
	Thing('Socks', 10, 35),
	Thing('Tissues', 15, 80),
	Thing('Phone', 500, 200),
	Thing('Baseball cap', 100, 70)
	] + THINGS

	POPULATION_SIZE = 10
	WEIGHT_LIMIT = 3000
	FITNESS_LIMIT = 740
	FITNESS_LIMIT_MORE_THINGS = 1310
	GENERATION_LIMIT = 100

	
	population, generations = run_evolution(

		#use partial to preset the paremeters to our currnt problem
		populate_func = partial(
			generate_population, size = POPULATION_SIZE, genome_length = len(MORE_THINGS)
		),
		fitness_func = partial(
			fitness, things=MORE_THINGS, weight_limit=WEIGHT_LIMIT
		),
		fitness_limit = FITNESS_LIMIT_MORE_THINGS,
		things = MORE_THINGS,
		generation_limit = GENERATION_LIMIT
	)

	print(f'''
	number of generations: {generations} 
	and population chosed:
	{genome_to_things(population[0], MORE_THINGS)}
	''')