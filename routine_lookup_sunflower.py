from drone_function import go_to_position
from routine_plant import routine_plant_find_available_position, routine_harvest_execute

def routine_lookup_place_sunflower(rows, cols, plantPattern, quantity):
  sunflowerPositions = []

  while quantity > 0:
    bestPositionY, bestPositionX = routine_plant_find_available_position(cols, rows, plantPattern)

    if (bestPositionY >= 0 and bestPositionX >= 0):
      plantPattern[bestPositionY][bestPositionX] = Entities.Sunflower
      sunflowerPositions.append((bestPositionY, bestPositionX))
      quantity -= 1

  return plantPattern, sunflowerPositions

def routine_lookup_harvest_sunflower(sunflowerPositions):
  if len (sunflowerPositions) == 0:
    return False

  sunFlowerPetals = []
  sunflowerPetalsPosition = []

  for sunflowerPosition in sunflowerPositions:
    y, x = sunflowerPosition

    quick_print("ENTROU AQUI 1: ", y, x)
    go_to_position(y, x)

    if get_entity_type() == Entities.Sunflower:
      if can_harvest():
        petals = measure()
        sunFlowerPetals.append(petals)
        sunflowerPetalsPosition.append((y, x))

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

      quick_print("Harvesting sunflower at position: ", y, x)

      go_to_position(y, x)
      routine_harvest_execute()

      sunFlowerPetals.pop(maxIndex)
      sunflowerPetalsPosition.pop(maxIndex)

  return True