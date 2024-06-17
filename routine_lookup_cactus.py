from drone_functions import go_to_position, go_to_position_swapping
from routine_resource import routine_get_cactus_seed

def routine_lookup_place_cactus(plantPattern, quantity):
  if quantity == 0:
    return plantPattern, [], {}

  centerY = 6
  centerX = 2

  cactusPositions = []
  cactusCompassPosition = {
    "North": { "x": centerX, "y": centerY + 1 },
    "East":  { "x": centerX + 1, "y": centerY },
    "West":  { "x": centerX - 1, "y": centerY },
    "South": { "x": centerX, "y": centerY - 1 },
  }

  plantPattern[centerY][centerX] = Entities.Cactus
  plantPattern[centerY][centerX + 1] = Entities.Cactus
  plantPattern[centerY][centerX - 1] = Entities.Cactus
  plantPattern[centerY + 1][centerX] = Entities.Cactus
  plantPattern[centerY - 1][centerX] = Entities.Cactus
  cactusPositions.append([centerY, centerX])
  cactusPositions.append([centerY, centerX + 1])
  cactusPositions.append([centerY, centerX - 1])
  cactusPositions.append([centerY + 1, centerX])
  cactusPositions.append([centerY - 1, centerX])
  quantity -= 5

  return plantPattern, cactusPositions, cactusCompassPosition

def routine_lookup_harvest_cactus(cactusPositions, cactusCompass):
  if num_items(Items.Cactus_Seed) < len(cactusPositions):
    return False

  if len(cactusPositions) == 0:
    return False

  orderToLook = ["West", "South", "North", "East"]
  isCactusInCompassComplete = {
    "North": False,
    "East": False,
    "West": False,
    "South": False,
  }

  for order in orderToLook:
    desiredSize = 0
    desiredCactusPosition = [0, 0]

    if order == "West" or order == "South":
      desiredSize = 9

    if order == "North" or order == "East":
      desiredSize = 0

    index = -1
    for cactusPosition in cactusPositions:
      index += 1
      y, x = cactusPosition

      if isCactusInCompassComplete["West"] == True and y == cactusCompass["West"]["y"] and x == cactusCompass["West"]["x"]:
        pass
      elif isCactusInCompassComplete["South"] == True and y == cactusCompass["South"]["y"] and x == cactusCompass["South"]["x"]:
        pass
      elif isCactusInCompassComplete["North"] == True and y == cactusCompass["North"]["y"] and x == cactusCompass["North"]["x"]:
        pass
      elif isCactusInCompassComplete["East"] == True and y == cactusCompass["East"]["y"] and x == cactusCompass["East"]["x"]:
        pass
      else:
        go_to_position(y, x)
        cactusSize = measure()

        if order == "West" or order == "South":
          if cactusSize == 0:
            desiredCactusPosition = [y, x]
            break
          elif cactusSize < desiredSize:
            desiredSize = cactusSize
            desiredCactusPosition = [y, x]
        elif order == "North" or order == "East":
          if cactusSize == 9:
            desiredCactusPosition = [y, x]
            break
          elif cactusSize > desiredSize:
            desiredSize = cactusSize
            desiredCactusPosition = [y, x]

    swap_cactus_to_position(desiredCactusPosition, cactusCompass[order])
    isCactusInCompassComplete[order] = True

  harvest()
  seedsQuantity = len(cactusPositions)
  routine_get_cactus_seed(seedsQuantity, seedsQuantity)
  for cactusPosition in cactusPositions:
      y, x = cactusPosition

      go_to_position(y, x)
      plant(Entities.Cactus)

def swap_cactus_to_position(desiredCactusPosition, orderPosition):
  indexY, indexX = desiredCactusPosition
  orderY, orderX = orderPosition["y"], orderPosition["x"]
  go_to_position(indexY, indexX)

  droneY = get_pos_y()
  droneX = get_pos_x()

  if droneY == orderY and droneX == orderX:
    return True

  centerX = 2

  droneY = get_pos_y()
  go_to_position_swapping(droneY, centerX)
  droneX = get_pos_x()
  go_to_position_swapping(orderY, droneX)
  droneY = get_pos_y()
  go_to_position_swapping(droneY, orderX)

  return True