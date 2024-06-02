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

