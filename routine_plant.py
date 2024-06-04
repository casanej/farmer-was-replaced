def routine_harvest_execute(block = True):

  if block:
    plant = get_entity_type()

    if(plant == Entities.Sunflower):
      return

  waterLevel = get_water()

  if (waterLevel < 0.5):
    use_item(Items.Water_Tank)

  if (can_harvest()):
    harvest()

def routine_soil_execute(entity = Entities.Grass):
  if (entity == Entities.Bush or entity == Entities.Tree or entity == Entities.Pumpkin or entity == Entities.Carrots or entity == Entities.Sunflower):
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

def routine_plant_plan_execute(cols, rows, plantPattern, entity):
  bestPositionScore = -1

  bestPositionY, bestPositionX = routine_plant_find_available_position(cols, rows, plantPattern)

  if (entity == Entities.Tree):
    for lookupBestY in range(cols):
      for lookupBestX in range(rows):

        canPlace = plantPattern[lookupBestY][lookupBestX] == None

        if (lookupBestX + 1 < rows):
          posRight = plantPattern[lookupBestY][lookupBestX+1]
        else:
          posRight = None

        if (lookupBestX - 1 >= 0):
          posLeft = plantPattern[lookupBestY][lookupBestX-1]
        else:
          posLeft = None

        if (lookupBestY + 1 < cols):
          posUp = plantPattern[lookupBestY+1][lookupBestX]
        else:
          posUp = None

        if (lookupBestY - 1 >= 0):
          posDown = plantPattern[lookupBestY-1][lookupBestX]
        else:
          posDown = None

        bestPositionLocalScore = 0

        if posUp != Entities.Tree:
          bestPositionLocalScore += 1
        if posRight != Entities.Tree:
          bestPositionLocalScore += 1
        if posDown != Entities.Tree:
          bestPositionLocalScore += 1
        if posLeft != Entities.Tree:
          bestPositionLocalScore += 1

        if (bestPositionLocalScore > bestPositionScore) and canPlace == True:
          bestPositionScore = bestPositionLocalScore
          bestPositionY = lookupBestY
          bestPositionX = lookupBestX

  if (bestPositionY >= 0 and bestPositionX >= 0):
    plantPattern[bestPositionY][bestPositionX] = entity

  return plantPattern



