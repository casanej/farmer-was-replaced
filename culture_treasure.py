from drone_functions import go_to_position
from routine_resource import routine_get_fertilizer
from maze_solver import maze_solver

def culture_treasure():
  while True:
    routine_get_fertilizer(100, 100)
    plant(Entities.Bush)

    isMaze = False

    while not isMaze:
      use_item(Items.Fertilizer)

      checkIfTreasure = get_entity_type() == Entities.Hedge or get_entity_type() == Entities.Treasure

      if checkIfTreasure:
        isMaze = True
        break

    maze_solver()

