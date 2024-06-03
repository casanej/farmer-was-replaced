from drone_function import go_to_position
from routine_plant import routine_plant_find_available_position, routine_harvest_execute, routine_plant_execute

def routine_lookup_place_sunflower(rows, cols, plantPattern, quantity):
  sunflowerPositions = []

  while quantity > 0:
    bestPositionY, bestPositionX = routine_plant_find_available_position(cols, rows, plantPattern)

    if (bestPositionY >= 0 and bestPositionX >= 0):
      plantPattern[bestPositionY][bestPositionX] = Entities.Sunflower
      sunflowerPositions.append((bestPositionY, bestPositionX))
      quantity -= 1

  return plantPattern, sunflowerPositions

def routine_lookup_harvest_sunflower(sunflowersPosition, totalSunFlowers):
  if len (sunflowersPosition) == 0:
    return False

  sunFlowerPetals = []
  sunflowerPetalsPosition = []

  allCanHarvest = False

  for sunflowerPosition in sunflowersPosition:
    y, x = sunflowerPosition

    go_to_position(y, x)

    if get_entity_type() == Entities.Sunflower:
      if can_harvest():
        petals = measure()
        sunFlowerPetals.append(petals)
        sunflowerPetalsPosition.append((y, x))

  allCanHarvest = len(sunFlowerPetals) == totalSunFlowers

  if not allCanHarvest:
    return False

  while len(sunFlowerPetals) != 0:
    maxPetals = max(sunFlowerPetals)
    maxIndex = -1

    for index in range(len(sunFlowerPetals)):
      value = sunFlowerPetals[index]
      if value == maxPetals:
        maxIndex = index
        break

    if maxIndex >= 0:
      y, x = sunflowerPetalsPosition[maxIndex]

      go_to_position(y, x)
      routine_harvest_execute()

      sunFlowerPetals.pop(maxIndex)
      sunflowerPetalsPosition.pop(maxIndex)

  routine_replant_sunflower(sunflowersPosition)
  return True

def routine_replant_sunflower(sunflowerPositions):
  if len(sunflowerPositions) == 0:
    return False

  for sunflowerPosition in sunflowerPositions:
    y, x = sunflowerPosition

    go_to_position(y, x)
    routine_plant_execute(Entities.Sunflower)

  return True