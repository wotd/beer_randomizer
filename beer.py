import random
import logging

from typing import List
from dataclasses import dataclass, field


logger = logging.getLogger("DRUNK_FELLAS")
GLUTEN_FREE_BEER = [52,53,54,55]
CELIACS = ['Zuza']

@dataclass
class Beer:
	is_gluten: bool
	name: str
	number: int

	# def __init__(self, name:str, number: int, is_gluten: bool = False):


class GlutenFreeException(Exception):
	pass


@dataclass
class DrunkDeveloper:

	name: str
	is_celiac: bool
	beer: Beer = field(default=None)

	def __init__(self, name: str, celiac: bool = False):
		self.name = name
		self.is_celiac = celiac

	def assign_beer(self, beer_num: int):
		if beer_num not in GLUTEN_FREE_BEER and self.is_celiac:
			raise GlutenFreeException()
		self.beer = get_beers()[beer_num-1]

	def __str__(self) -> str:
		return f"{self.name} -> {self.beer}"

def randomize_beer(beers: List[Beer], people: List[DrunkDeveloper]):
	"""
	Tell who is going to get drunk first

	:param nr_beers: 
	"""

	for person in people:

		while True:
			try:
				person.assign_beer(random.randint(1, len(beers)))
				break
			except GlutenFreeException:
				continue
		logger.info("{0!s} picked {1!s} beer".format(person.name, person.beer.name))
		# logging.info(person)

def get_beers():
	beers = []
	for number in range(1,55):
		beers.append(Beer("Beer %s" % number, number, number>51))
	return beers

def get_developers():
	return [DrunkDeveloper(name, name in CELIACS) 
	    for name in ['Kathe','Zrebak','Jesse','Martijn', 'Norbi', 'Jaczek', 'Eduardo', 'Zuza']]
	

if __name__ == "__main__":
	logging.basicConfig(level=logging.INFO)

	# randomize beer
	randomize_beer(get_beers(), get_developers())
