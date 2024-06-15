def routine_lookup_place_pumpkin(rows, cols, plantPattern, quantity):
  restPumpkin = quantity

  while restPumpkin >= 4:
    pumpkinSquare = 0
    for y in range(cols):
      if (y == 0 or y == 1):
        continue

      if (y * y) > restPumpkin:
        break

      pumpkinSquare = y

    restPumpkin -= pumpkinSquare * pumpkinSquare

    plantPattern = lookup_pumpkin_search_square(plantPattern, cols, rows, pumpkinSquare)

  plantPattern = lookup_pumpkin_add_anywhere(plantPattern, cols, rows, restPumpkin)

  return plantPattern

def lookup_pumpkin_search_square(plantPattern, cols, rows, squareSize):
  posSquareXAvailable = -1
  posSquareYAvailable = -1
  wasFound = False

  for y in range(cols):
    for x in range(rows):
      if plantPattern[y][x] == None:
        if x + squareSize > rows or y + squareSize > cols:
          continue

        posSquareXAvailable = x
        posSquareYAvailable = y
        wasFound = True
        break

    if wasFound:
      break

  if posSquareXAvailable == -1:
    return lookup_pumpkin_add_anywhere(plantPattern, cols, rows, squareSize * squareSize)

  for y in range(squareSize):
    for x in range(squareSize):
      plantPattern[y + posSquareYAvailable][x + posSquareXAvailable] = Entities.Pumpkin

  return plantPattern

def lookup_pumpkin_add_anywhere(plantPattern, cols, rows, quantity):
  for y in range(cols):
    if quantity == 0:
      break
    for x in range(rows):
      if quantity == 0:
        break

      canPlace = plantPattern[y][x] == None

      if canPlace:
        plantPattern[y][x] = Entities.Pumpkin
        quantity -= 1

  return plantPattern