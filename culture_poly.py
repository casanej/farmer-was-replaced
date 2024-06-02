from routine_plant import routine_harvest_execute, routine_soil_execute, routine_plant_execute
from routine_resource import routine_get_carrot_seed, routine_get_pumpkin_seed, routine_get_tank, routine_get_sunflower

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
			if grass > 0:
				plantRow.append(Entities.Grass)
				grass -= 1
			elif bush > 0:
				plantRow.append(Entities.Bush)
				bush -= 1
			elif carrot > 0:
				plantRow.append(Entities.Carrots)
				carrot -= 1
			elif pumpkin > 0:
				plantRow.append(Entities.Pumpkin)
				pumpkin -= 1
			elif tree > 0:
				plantRow.append(Entities.Tree)
				tree -= 1
			elif sunflower > 0:
				plantRow.append(Entities.Sunflower)
				sunflower -= 1
			elif cactus > 0:
				plantRow.append(Entities.Cactus)
				cactus -= 1
			else:
				plantRow.append(Entities.Grass)

		plantPattern.append(plantRow)

	clear()
	do_a_flip()

	for x in range(rows):
			for y in range(columns):
				droneXPos = get_pos_x()
				droneYPos = get_pos_y()

				plant = plantPattern[droneYPos][droneXPos]

				routine_soil_execute(plant)
				routine_plant_execute(plant)

				move(North)
			move(East)

	while True:
		for x in range(rows):
			for y in range(columns):
				droneXPos = get_pos_x()
				droneYPos = get_pos_y()

				plant = plantPattern[droneYPos][droneXPos]

				routine_harvest_execute(plant)

				move(North)
			move(East)
			routine_get_carrot_seed(12, 12)
			routine_get_pumpkin_seed(12, 12)
			routine_get_sunflower(12, 12)
			routine_get_tank(100, 100)



