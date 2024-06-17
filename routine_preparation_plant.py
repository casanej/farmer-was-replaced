from routine_lookup_tree import routine_lookup_place_tree
from routine_lookup_place import routine_lookup_place_pumpkin
from routine_lookup_cactus import routine_lookup_place_cactus
from routine_lookup_dinosaur import routine_lookup_place_dinosaur
from routine_lookup_sunflower import routine_lookup_place_sunflower
from routine_plant import routine_plant_plant_execute, routine_soil_execute, routine_plant_watering

def routine_plant_pattern(rows=1, columns=1, grass=0, bush=0, carrot=0, pumpkin=0, tree = 0, sunflower = 0, cactus = 0, dinosaur = 0):
  spaces = rows * columns
  divisorGrass = 0

  if grass == 0 and bush == 0 and carrot == 0 and pumpkin == 0 and sunflower == 0 and cactus == 0 and dinosaur == 0:
    print("Error: Must have at least one plant.")
    return [], [], [], {}, 0, 0, 0, 0, 0

  if cactus > 0:
    if cactus != 5:
      print("Error: Cactus quantity must be 5.")
      return [], [], [], {}, 0, 0, 0, 0, 0

  if dinosaur > 0:
    if dinosaur != rows:
      print("Error: Dinosaur quantity must be the same as the number of rows.")
      return [], [], [], {}, 0, 0, 0, 0, 0

    divisorGrass = dinosaur

  totalEntities = grass + bush + carrot + pumpkin + tree + sunflower + cactus + dinosaur + divisorGrass

  if totalEntities > spaces:
    print("Error: Not enough spaces for the plants.")
    return [], [], [], {}, 0, 0, 0, 0, 0

  grass = max(0, grass - divisorGrass)

  seedsCarrot = max(0, carrot)
  seedsPumpkin = max(0, pumpkin)
  seedsSunflower = max(0, sunflower)
  seedsCactus = max(0, cactus)
  dinosaurEggs = max(0, dinosaur)

  totalSpaces = rows * columns

  plantPattern = []
  sunflowersPosition = []

  for y in range(columns):
    plantRow = []
    for x in range(rows):
      plantRow.append(None)
    plantPattern.append(plantRow)

  dinosaurCol = columns - 1
  remainingGrass = totalSpaces - totalEntities

  plantPattern = routine_lookup_place_dinosaur(dinosaurCol, rows, plantPattern, dinosaur)
  plantPattern = routine_lookup_place_pumpkin(rows, columns, plantPattern, pumpkin)
  plantPattern, cactusPosition, cactusCompass = routine_lookup_place_cactus(plantPattern, cactus)
  plantPattern = routine_lookup_place_tree(rows, columns, plantPattern, tree)
  plantPattern = routine_plant_plant_execute(rows, columns, plantPattern, 0, bush, carrot)
  plantPattern, sunflowersPosition = routine_lookup_place_sunflower(rows, columns, plantPattern, sunflower)
  plantPattern = routine_plant_plant_execute(rows, columns, plantPattern, grass, 0, 0)
  plantPattern = routine_plant_plant_execute(rows, columns, plantPattern, remainingGrass, 0, 0)

  return plantPattern, sunflowersPosition, cactusPosition, cactusCompass, seedsCarrot, seedsPumpkin, seedsSunflower, seedsCactus, dinosaurEggs

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