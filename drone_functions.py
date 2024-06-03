def go_to_position(y, x):
  dronePosX = get_pos_x()
  dronePosY = get_pos_y()

  if dronePosX < x:
    for e in range(x - dronePosX):
      move(East)
  elif dronePosX > x:
    for w in range(dronePosX - x):
      move(West)

  if dronePosY < y:
    for s in range(y - dronePosY):
      move(South)
  elif dronePosY > y:
    for n in range(dronePosY - y):
      move(North)