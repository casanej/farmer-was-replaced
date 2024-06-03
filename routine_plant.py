def routine_harvest_execute(entity = Entities.Grass):

  if (can_harvest()):
    harvest()
    plant(entity)
  else:
    if (get_entity_type() == None):
      plant(entity)

def routine_soil_execute(entity = Entities.Grass):
  if (get_entity_type() != None):
    harvest()

  if (entity == Entities.Pumpkin or entity == Entities.Carrots or entity == Entities.Sunflower):
    if get_ground_type() == Grounds.Turf:
      till()

def routine_plant_execute(entity = Entities.Grass):
  if (get_entity_type() != None):
    harvest()

  if (entity == Entities.Pumpkin or entity == Entities.Carrots or entity == Entities.Sunflower):
    if get_ground_type() != Grounds.Turf:
      plant(entity)
    else:
      print("Cannot plant on this ground type")

def routine_plant_plan_execute(cols, rows, plantPattern, entity, isOdd = False):
  bestPositionX = 0
  bestPositionY = 0
  bestPositionScore = -1

  for initialBestY in range(cols):
    for initialBestX in range(rows):
      if plantPattern[initialBestY][initialBestX] == None:
        bestPositionX = initialBestX
        bestPositionY = initialBestY
        bestPositionScore = 0
        break

  if (entity == Entities.Pumpkin or entity == Entities.Tree):
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

        if (entity == Entities.Pumpkin):
          if posUp == Entities.Pumpkin:
            if isOdd:
              bestPositionLocalScore += 10
            else:
              bestPositionLocalScore += 1
          if posRight == Entities.Pumpkin:
            bestPositionLocalScore += 1
          if posDown == Entities.Pumpkin:
            bestPositionLocalScore += 1
          if posLeft == Entities.Pumpkin:
            if isOdd:
              bestPositionLocalScore += 1
            else:
              bestPositionLocalScore += 10

        elif (entity == Entities.Tree):
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

  plantPattern[bestPositionY][bestPositionX] = entity

  return plantPattern



