from culture_poly import culture_poly

willStop = False
size = get_world_size()
rows = size
cols = size

while willStop == False:
	grass = 0
	bush = 0
	carrot = 20
	pumpkin = 24
	tree = 10
	sunflower = 32
	cactus = 0
	willStop = culture_poly(rows, cols, grass, bush, carrot, pumpkin, tree, sunflower, cactus)