from routine_lookup_tree import routine_lookup_place_tree
from routine_lookup_place import routine_lookup_place_pumpkin
from routine_lookup_cactus import routine_lookup_place_cactus
from routine_lookup_sunflower import routine_lookup_place_sunflower
from routine_plant import routine_plant_plant_execute, routine_soil_execute, routine_plant_watering

def routine_plant_pattern(rows=1, columns=1, grass=0, bush=0, carrot=0, pumpkin=0, tree = 0, sunflower = 0, cactus = 0):
  spaces = rows * columns

  if grass == 0 and bush == 0 and carrot == 0 and pumpkin == 0 and sunflower == 0 and cactus == 0:
    print("Error: Must have at least one plant.")
    return [], [], 0, 0, 0

  if (grass + bush + carrot + pumpkin + sunflower + cactus) > spaces:
    print("Error: Not enough spaces for the plants.")
    return [], [], 0, 0, 0

  if cactus > 0:
    if cactus != 5:
      print("Error: Cactus quantity must be 5.")
      return [], [], 0, 0, 0

  seedsCarrot = max(0, carrot)
  seedsPumpkin = max(0, pumpkin)
  seedsSunflower = max(0, sunflower)
  seedsCactus = max(0, cactus)

  totalSpaces = rows * columns

  plantPattern = []
  sunflowersPosition = []

  for y in range(columns):
    plantRow = []
    for x in range(rows):
      plantRow.append(None)
    plantPattern.append(plantRow)


  plantPattern = routine_lookup_place_pumpkin(rows, columns, plantPattern, pumpkin)
  plantPattern, cactusPosition, cactusCompass = routine_lookup_place_cactus(rows, columns, plantPattern, cactus)
  plantPattern = routine_lookup_place_tree(rows, columns, plantPattern, tree)
  plantPattern, sunflowersPosition = routine_lookup_place_sunflower(rows, columns, plantPattern, sunflower)

  totalGrass = grass + (totalSpaces - (pumpkin + tree + sunflower + cactus))

  plantPattern = routine_plant_plant_execute(rows, columns, plantPattern, totalGrass, bush, carrot)

  return plantPattern, sunflowersPosition, cactusPosition, cactusCompass, seedsCarrot, seedsPumpkin, seedsSunflower, seedsCactus

def routine_prepare_soil(plantPattern):
  rows = len(plantPattern)
  columns = len(plantPattern[0])

  for x in range(rows):
    for y in range(columns):
      droneXPos = get_pos_x()
      droneYPos = get_pos_y()

      plant = plantPattern[droneYPos][droneXPos]

      routine_soil_execute(plant)
      routine_plant_watering()

      move(North)
    move(East)