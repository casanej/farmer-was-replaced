def culture_row():
	gridSizeX = 7
	gridSizeY = 7

	droneXPos = 0
	droneYPos = 0

	plantPattern = [
		[Entities.Grass, Entities.Tree, Entities.Grass, Entities.Tree, Entities.Grass, Entities.Tree, Entities.Grass],
		[Entities.Tree, Entities.Grass, Entities.Tree, Entities.Grass, Entities.Tree, Entities.Grass, Entities.Tree],
		[Entities.Grass, Entities.Tree, Entities.Grass, Entities.Tree, Entities.Grass, Entities.Tree, Entities.Grass],
		[Entities.Tree, Entities.Grass, Entities.Tree, Entities.Grass, Entities.Tree, Entities.Grass, Entities.Tree],
		[Entities.Grass, Entities.Tree, Entities.Grass, Entities.Tree, Entities.Grass, Entities.Tree, Entities.Grass],
		[Entities.Tree, Entities.Grass, Entities.Tree, Entities.Grass, Entities.Tree, Entities.Grass, Entities.Tree],
		[Entities.Grass, Entities.Tree, Entities.Grass, Entities.Tree, Entities.Grass, Entities.Tree, Entities.Grass],
	]

	for x in range(gridSizeX):
		for y in range(gridSizeY):
			droneXPos = get_pos_x()
			droneYPos = get_pos_y()

			plant = plantPattern[droneYPos][droneXPos]

			routine_harvest_execute(plant)

			move(North)
		move(East)
		routine_get_carrot_seed(12, 12)
		routine_get_pumpkin_seed(12, 12)
		routine_get_tank(100, 5)