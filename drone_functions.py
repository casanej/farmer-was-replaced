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


def check_possible_directions(backtrace):
  directions = [North, East, South, West]
  possibleDirections = []

  for direction in directions:
    wrongWay = False

    if (len(backtrace) > 0):
      wrongWay = is_inverse_direction(direction, backtrace[len(backtrace) - 1])

    if (wrongWay):
      continue

    moved, oldPos, newPos = check_if_can_move(direction)

    if not moved:
      continue

    if moved:
      possibleDirections.append(direction)
      y, x = oldPos
      go_to_position(y, x)

  return possibleDirections


def current_position():
  return get_pos_y(), get_pos_x()


def check_if_can_move(direction):
  oldPos = (get_pos_y(), get_pos_x())
  canMove = move(direction)
  newPos = (get_pos_y(), get_pos_x())

  return canMove, oldPos, newPos


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
