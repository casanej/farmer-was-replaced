def routine_lookup_place_pumpkin(rows, cols, plantPattern, quantity):
  highPumpkinSquare = 0

  for y in range(cols):
    if y == 0:
      continue

    if (y * y) > quantity:
      break

    highPumpkinSquare = y

  restPumpkin = quantity - (highPumpkinSquare * highPumpkinSquare)

  for y in range(highPumpkinSquare):
    for x in range(highPumpkinSquare):
      plantPattern[y][x] = Entities.Pumpkin

  for y in range(cols):
    for x in range(rows):
      if restPumpkin == 0:
        break

      canPlace = plantPattern[y][x] == None

      if canPlace:
        plantPattern[y][x] = Entities.Pumpkin
        restPumpkin -= 1
        continue

  return plantPattern