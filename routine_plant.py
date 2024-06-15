def routine_harvest_execute(block = True):

  if block:
    plant = get_entity_type()

    if(plant == Entities.Sunflower or plant == Entities.Cactus):
      return

  routine_plant_watering()

  if (can_harvest()):
    harvest()

def routine_soil_execute(entity = Entities.Grass):
  if (entity != Entities.Grass):
    if get_ground_type() == Grounds.Turf:
      till()

def routine_plant_execute(entity = Entities.Grass):
  canPlant = False

  if get_entity_type() == None:
    canPlant = True

  if (entity == Entities.Pumpkin or entity == Entities.Carrots or entity == Entities.Sunflower):
    if get_ground_type() == Grounds.Turf:
      canPlant = False
      print("Cannot plant on this ground type")

  if canPlant:
    plant(entity)

def routine_plant_watering():
  waterLevel = get_water()

  if (waterLevel < 0.5):
    use_item(Items.Water_Tank)

def routine_plant_fertilize():
  use_item(Items.Water_Tank)
  if (can_harvest()):
    use_item(Items.Fertilizer)
    use_item(Items.Water_Tank)

def routine_plant_find_available_position(cols, rows, plantPattern):
  bestPositionX = -1
  bestPositionY = -1
  hasFoundBestPosition = False

  for initialBestY in range(cols):
    for initialBestX in range(rows):
      if plantPattern[initialBestY][initialBestX] == None:
        bestPositionX = initialBestX
        bestPositionY = initialBestY
        hasFoundBestPosition = True
        break

    if hasFoundBestPosition:
      break

  return bestPositionY, bestPositionX

def routine_plant_plant_execute(cols, rows, plantPattern, entity):
  bestPositionY, bestPositionX = routine_plant_find_available_position(cols, rows, plantPattern)

  if (bestPositionY >= 0 and bestPositionX >= 0):
    plantPattern[bestPositionY][bestPositionX] = entity

  return plantPattern
