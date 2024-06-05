from routine_lookup_place import routine_lookup_place_pumpkin
from routine_lookup_sunflower import routine_lookup_place_sunflower
from routine_plant import routine_plant_plan_execute, routine_soil_execute, routine_plant_watering

def routine_plant_pattern(rows=1, columns=1, grass=0, bush=0, carrot=0, pumpkin=0, tree = 0, sunflower = 0, cactus = 0):
  spaces = rows * columns

  if grass == 0 and bush == 0 and carrot == 0 and pumpkin == 0 and sunflower == 0 and cactus == 0:
    return [], [], 0, 0, 0

  if (grass + bush + carrot + pumpkin + sunflower + cactus) > spaces:
    print("Error: Not enough spaces for the plants.")
    return [], [], 0, 0, 0

  seedsCarrot = max(0, carrot)
  seedsPumpkin = max(0, pumpkin)
  seedsSunflower = max(0, sunflower)

  plantPattern = []
  sunflowersPosition = []
  positionFilled = 0

  allSpacesFilled = False

  for x in range(rows):
    plantRow = []
    for y in range(columns):
      plantRow.append(None)
    plantPattern.append(plantRow)

  while not allSpacesFilled:
    if pumpkin > 0:
      plantPattern = routine_lookup_place_pumpkin(rows, columns, plantPattern, pumpkin)
      pumpkin -= pumpkin
    elif tree > 0:
      plantPattern = routine_plant_plan_execute(rows, columns, plantPattern, Entities.Tree)
      tree -= 1
    elif bush > 0:
      plantPattern = routine_plant_plan_execute(rows, columns, plantPattern, Entities.Bush)
      bush -= 1
    elif carrot > 0:
      plantPattern = routine_plant_plan_execute(rows, columns, plantPattern, Entities.Carrots)
      carrot -= 1
    elif cactus > 0:
      plantPattern = routine_plant_plan_execute(rows, columns, plantPattern, Entities.Cactus)
      cactus -= 1
    elif sunflower > 0:
      newPlantPattern, sunflowersPosition = routine_lookup_place_sunflower(rows, columns, plantPattern, sunflower)
      plantPattern = newPlantPattern
      sunflower -= sunflower
    else:
      plantPattern = routine_plant_plan_execute(rows, columns, plantPattern, Entities.Grass)

    positionFilled += 1

    if positionFilled == spaces:
      allSpacesFilled = True

  return plantPattern, sunflowersPosition, seedsCarrot, seedsPumpkin, seedsSunflower

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