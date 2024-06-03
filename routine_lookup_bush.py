from drone_functions import go_to_position
from routine_plant import routine_plant_find_available_position, routine_plant_fertilize, routine_harvest_execute, routine_plant_execute

def routine_lookup_place_bush(rows, cols, plantPattern, quantity):
  bushesPosition = []

  while quantity > 0:
    y, x = routine_plant_find_available_position(cols, rows, plantPattern)

    if (y >= 0 and x >= 0):
      plantPattern[y][x] = Entities.Bush
      bushesPosition.append((y, x))
      quantity -= 1

  return plantPattern, bushesPosition

def routine_lookup_fertilize_bush(bushesPosition):
  for bushPosition in bushesPosition:
    y, x = bushPosition

    go_to_position(y, x)
    routine_plant_fertilize()
    quick_print("Teste", get_entity_type())

    if (get_entity_type() == Entities.Treasure or get_entity_type() == Entities.Hedge):
      while True:
        quick_print(measure())
        do_a_flip()
    else:
      routine_harvest_execute()
      routine_plant_execute(Entities.Bush)
