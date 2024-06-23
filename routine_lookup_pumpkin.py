from drone_functions import go_to_position

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
  quick_print("Harvesting pumpkins", len(pumpkinsSquareLocation))
  pumpkinsMissed = -1

  while pumpkinsMissed != 0:
    pumpkinsMissed = 0

    for location in pumpkinsSquareLocation:
      y, x = location
      go_to_position(x, y)

      if get_entity_type() != Entities.Pumpkin:
        pumpkinsMissed += 1
        plant(Entities.Pumpkin)


  go_to_position(0, 0)
  harvest()

  return True