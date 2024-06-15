def routine_lookup_place_tree(rows, cols, plantPattern, quantity):
  for y in range(cols):
    if quantity == 0:
        break

    isPairColumn = y % 2 == 0

    for x in range(rows):
      if quantity == 0:
        break

      canPlace = plantPattern[y][x] == None

      if canPlace:
        if isPairColumn:
          if x % 2 == 0:
            plantPattern[y][x] = Entities.Tree
            quantity -= 1
        else:
          if x % 2 != 0:
            plantPattern[y][x] = Entities.Tree
            quantity -= 1

  return plantPattern