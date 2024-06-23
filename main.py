from culture_poly import culture_poly
from culture_treasure import culture_treasure

willStop = False
size = get_world_size()
rows = size
cols = size

while willStop == False:
	grass = 0
	bush = 0
	carrot = 0
	pumpkin = rows * cols
	tree = 0
	sunflower = 0
	cactus = 0
	dinosaur = 0
	willStop = culture_poly(rows, cols, grass, bush, carrot, pumpkin, tree, sunflower, cactus, dinosaur)