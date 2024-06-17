from culture_poly import culture_poly
from culture_treasure import culture_treasure

willStop = False
size = get_world_size()
rows = size
cols = size

while willStop == False:
	grass = 0
	bush = 0
	carrot = 18
	pumpkin = 22
	tree = 10
	sunflower = 25
	cactus = 5
	dinosaur = size
	willStop = culture_poly(rows, cols, grass, bush, carrot, pumpkin, tree, sunflower, cactus, dinosaur)