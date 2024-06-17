def go_to_position(y, x):
  isDroneAtPosition = False

  while not isDroneAtPosition:
    dronePosX = get_pos_x()
    dronePosY = get_pos_y()

    while not dronePosX == x:
      if dronePosX < x:
        move(East)
      elif dronePosX > x:
        move(West)

      dronePosX = get_pos_x()

    while not dronePosY == y:
      if dronePosY > y:
        move(South)
      elif dronePosY < y:
        move(North)

      dronePosY = get_pos_y()

    isDroneAtPosition = dronePosX == x and dronePosY == y

def go_to_position_swapping(y, x):
  isDroneAtPosition = False

  while not isDroneAtPosition:
    dronePosX = get_pos_x()
    dronePosY = get_pos_y()

    while not dronePosX == x:
      if dronePosX < x:
        swap(East)
        move(East)
      elif dronePosX > x:
        swap(West)
        move(West)

      dronePosX = get_pos_x()

    while not dronePosY == y:
      if dronePosY > y:
        swap(South)
        move(South)
      elif dronePosY < y:
        swap(North)
        move(North)

      dronePosY = get_pos_y()

    isDroneAtPosition = dronePosX == x and dronePosY == y

def inverse_direction(direction):
  if direction == North:
    return South
  elif direction == South:
    return North
  elif direction == East:
    return West
  elif direction == West:
    return East
  else:
    return None


def is_inverse_direction(direction1, direction2):
  return inverse_direction(direction1) == direction2

def measure_direction(direction = "Center"):
  if direction == "North":
    return measure(North)
  elif direction == "South":
    return measure(South)
  elif direction == "East":
    return measure(East)
  elif direction == "West":
    return measure(West)
  else:
    return measure()