from drone_functions import check_possible_directions, inverse_direction, current_position


def create_default_tile(id, backDirection, lastTile, isStart=False):
	return {
		"id": id,
		"isStart": isStart,
		"directions": {
			North: None,
			East: None,
			South: None,
			West: None,
		},
		"backDirection": backDirection,
		"lastTile": lastTile,
	}


def maze_solver():
	currentId = 0
	tiles = {0: create_default_tile(0, None, 0, True)}

	isTreasure = get_entity_type() == Entities.Treasure
	directions = [North, East, South, West]

	while not isTreasure:
		currentTile = tiles[currentId]

		allDirectionsVisited = currentTile["directions"][North] != None and currentTile["directions"][
			East] != None and currentTile["directions"][South] != None and currentTile["directions"][West] != None

		if allDirectionsVisited and currentId != 0:
			currentId = currentTile["lastTile"]
			move(currentTile["backDirection"])
			continue

		for direction in directions:
			if currentTile["directions"][direction] == None:
				if move(direction):
					currentTile['directions'][direction] = True

					inverseDirection = inverse_direction(direction)

					nextTile = create_default_tile(currentId + 1, inverseDirection, currentId)
					nextTile["directions"][inverseDirection] = True
					nextTile["lastTile"] = currentId

					tiles[nextTile["id"]] = nextTile

					currentId = nextTile["id"]
					break

				else:
					currentTile['directions'][direction] = False

					if allDirectionsVisited:
						currentId = currentTile["lastTile"]
					break
			else:
				continue

		isTreasure = get_entity_type() == Entities.Treasure

	harvest()


maze_solver()
