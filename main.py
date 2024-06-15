from culture_poly import culture_poly

willStop = False
size = get_world_size()
rows = size
cols = size

while willStop == False:
	grass = 0
	bush = 0
	carrot = 16
	pumpkin = 18
	tree = 9
	sunflower = 12
	cactus = 5
	willStop = culture_poly(rows, cols, grass, bush, carrot, pumpkin, tree, sunflower, cactus)