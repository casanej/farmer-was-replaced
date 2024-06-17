from drone_functions import go_to_position
from routine_plant import routine_harvest_execute, routine_plant_execute
from routine_resource import routine_get_carrot_seed, routine_get_pumpkin_seed, routine_get_tank, routine_get_sunflower, routine_get_cactus_seed, routine_get_eggs
from routine_lookup_cactus import routine_lookup_harvest_cactus
from routine_lookup_dinosaur import routine_lookup_rearrange_group
from routine_lookup_sunflower import routine_lookup_harvest_sunflower
from routine_preparation_plant import routine_plant_pattern, routine_prepare_soil

def culture_poly(rows=1, columns=1, grass=0, bush=0, carrot=0, pumpkin=0, tree = 0, sunflower = 0, cactus = 0, dinosaur = 0):
	if rows < 1 or columns < 1:
		print("Error: Rows and columns must be greater than 0.")
		return True

	totalSpaces = rows * columns

	plantPattern, sunflowersPosition, cactusPosition, cactusCompass, seedsCarrot, seedsPumpkin, seedsSunflower, seedsCactus, dinosaurEggs = routine_plant_pattern(rows, columns, grass, bush, carrot, pumpkin, tree, sunflower, cactus, dinosaur)

	dinosaurCol = columns - 1

	go_to_position(0, 0)
	routine_prepare_soil(plantPattern)

	while True:
		go_to_position(0, 0)
		routine_get_carrot_seed(seedsCarrot, seedsCarrot * 2)
		routine_get_pumpkin_seed(seedsPumpkin, seedsPumpkin * 2)
		routine_get_cactus_seed(seedsCactus * 2, seedsCactus * 2)
		routine_get_sunflower(seedsSunflower, seedsSunflower * 2)
		routine_get_eggs(dinosaurEggs, dinosaurEggs * 2)
		routine_get_tank(totalSpaces, totalSpaces)
		for x in range(rows):
			for y in range(columns):
				droneXPos = get_pos_x()
				droneYPos = get_pos_y()

				plant = plantPattern[droneYPos][droneXPos]

				routine_harvest_execute()
				routine_plant_execute(plant)

				move(North)
			move(East)

		routine_lookup_rearrange_group(dinosaurCol, rows)
		routine_lookup_harvest_sunflower(sunflowersPosition)
		repeatCactus = 20
		while repeatCactus > 0:
			repeatCactus -= 1
			routine_lookup_harvest_cactus(cactusPosition, cactusCompass)

