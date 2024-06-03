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