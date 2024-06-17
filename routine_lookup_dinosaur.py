from drone_functions import go_to_position, go_to_position_swapping

def routine_lookup_place_dinosaur(col, rows, plantPattern, quantity):
  if quantity == 0:
    return plantPattern

  if quantity != rows:
    print("Error: Dinosaur quantity must be the same as the number of rows.")
    return [], []

  for x in range(rows):
    plantPattern[col][x] = Items.Egg

  for x in range(rows):
    plantPattern[col - 1][x] = Entities.Grass

  return plantPattern

def routine_lookup_stop_dinosaur(col, rows):
  measures = []
  for x in range(rows):
    go_to_position(col, x)
    measures.append(measure())

  quick_print("Measures: ", measures)

def routine_lookup_rearrange_group(col, rows):
  if num_items(Items.Egg) <= rows - 1:
    return

  lookingSize = 3
  availableSpot = 0

  routine_lookup_stop_dinosaur(col, rows)

  while lookingSize > -1:
    currentIndex = -1

    if availableSpot >= rows:
      break

    for x in range(rows):
      go_to_position(col, x)

      size = measure()
      if x >= availableSpot and size == lookingSize:
        currentIndex = x
        break

    routine_lookup_stop_dinosaur(col, rows)

    if currentIndex == -1:
      lookingSize -= 1
    else:
      go_to_position(col, currentIndex)
      go_to_position_swapping(col, availableSpot)
      availableSpot += 1

    routine_lookup_stop_dinosaur(col, rows)

  for x in range(rows):
    go_to_position(col, x)
    harvest()
    use_item(Items.Egg)