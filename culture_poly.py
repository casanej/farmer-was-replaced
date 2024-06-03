from drone_functions import go_to_position
from routine_plant import routine_harvest_execute, routine_soil_execute, routine_plant_execute, routine_plant_plan_execute
from routine_resource import routine_get_carrot_seed, routine_get_pumpkin_seed, routine_get_tank, routine_get_sunflower, routine_get_fertilizer
from routine_lookup_place import routine_lookup_place_pumpkin
from routine_lookup_bush import routine_lookup_place_bush, routine_lookup_fertilize_bush
from routine_lookup_sunflower import routine_lookup_place_sunflower, routine_lookup_harvest_sunflower

def culture_poly(rows=1, columns=1, grass=0, bush=0, carrot=0, pumpkin=0, tree = 0, sunflower = 0, cactus = 0):
	if rows < 1 or columns < 1:
		print("Error: Rows and columns must be greater than 0.")
		return True

	if grass == 0 and bush == 0 and carrot == 0 and pumpkin == 0 and sunflower == 0 and cactus == 0:
		return True

	spaces = rows * columns

	if (grass + bush + carrot + pumpkin + sunflower + cactus) > spaces:
		print("Error: Not enough spaces for the plants.")
		return

	plantPattern = []

	for x in range(rows):
		plantRow = []
		for y in range(columns):
			plantRow.append(None)
		plantPattern.append(plantRow)

	allSpacesFilled = False
	positionFilled = 0
	sunflowersPosition = []
	bushesPosition = []

	routine_get_carrot_seed(carrot, carrot)
	routine_get_pumpkin_seed(pumpkin, pumpkin)
	routine_get_sunflower(sunflower, sunflower)

	while not allSpacesFilled:
		if pumpkin > 0:
			plantPattern = routine_lookup_place_pumpkin(rows, columns, plantPattern, pumpkin)
			pumpkin -= pumpkin
		elif tree > 0:
			plantPattern = routine_plant_plan_execute(rows, columns, plantPattern, Entities.Tree)
			tree -= 1
		elif bush > 0:
			newPlantPattern, bushesPosition = routine_lookup_place_bush(rows, columns, plantPattern, bush)
			bush -= bush
		elif carrot > 0:
			plantPattern = routine_plant_plan_execute(rows, columns, plantPattern, Entities.Carrots)
			carrot -= 1
		elif cactus > 0:
			plantPattern = routine_plant_plan_execute(rows, columns, plantPattern, Entities.Cactus)
			cactus -= 1
		elif sunflower > 0:
			newPlantPattern, sunflowersPosition = routine_lookup_place_sunflower(rows, columns, plantPattern, sunflower)
			plantPattern = newPlantPattern
			sunflower -= sunflower
		else:
			plantPattern = routine_plant_plan_execute(rows, columns, plantPattern, Entities.Grass)

		positionFilled += 1

		if positionFilled == spaces:
			allSpacesFilled = True

	go_to_position(0, 0)
	for x in range(rows):
			for y in range(columns):
				droneXPos = get_pos_x()
				droneYPos = get_pos_y()

				plant = plantPattern[droneYPos][droneXPos]

				routine_soil_execute(plant)

				move(North)
			move(East)

	while True:
		go_to_position(0, 0)
		for x in range(rows):
			for y in range(columns):
				droneXPos = get_pos_x()
				droneYPos = get_pos_y()

				plant = plantPattern[droneYPos][droneXPos]

				routine_harvest_execute()

				routine_plant_execute(plant)

				move(North)
			move(East)

		routine_get_carrot_seed(12, 12)
		routine_get_pumpkin_seed(12, 12)
		routine_get_sunflower(12, 12)
		routine_get_tank(100, 100)
		routine_get_fertilizer(100, 100)
		go_to_position(7, 7)
		do_a_flip()
		do_a_flip()
		routine_lookup_harvest_sunflower(sunflowersPosition, len(sunflowersPosition))
		routine_lookup_fertilize_bush(bushesPosition)

