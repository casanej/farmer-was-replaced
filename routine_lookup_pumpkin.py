from drone_functions import go_to_position
from routine_plant import routine_plant_watering

def routine_lookup_place_pumpkin(rows, cols, plantPattern, quantity):
  pumpkinsSquareLocation = []
  squareSize = 0

  for y in range(1, cols + 1):
    squareQuantity = y * y
    if squareQuantity <= quantity:
      squareSize = y

  for y in range(squareSize):
    for x in range(squareSize):
      plantPattern[y][x] = Entities.Pumpkin
      pumpkinsSquareLocation.append([y, x])

  return plantPattern, pumpkinsSquareLocation

def routine_lookup_pumpkin_harvest(pumpkinsSquareLocation):
  pumpkinsMissed = []

  for location in pumpkinsSquareLocation:
    y, x = location
    go_to_position(x, y)
    routine_plant_watering()

    if get_entity_type() != Entities.Pumpkin:
      pumpkinsMissed.append(location)
      plant(Entities.Pumpkin)

  while len(pumpkinsMissed) != 0:
    pumpkinsMissedCheck = []

    for location in pumpkinsMissed:
      y, x = location
      go_to_position(x, y)

      if get_entity_type() != Entities.Pumpkin:
        pumpkinsMissedCheck.append(location)
        use_item(Items.Water_Tank)
        plant(Entities.Pumpkin)
        use_item(Items.Fertilizer)

    pumpkinsMissed = pumpkinsMissedCheck

  go_to_position(0, 0)
  harvest()

  return True