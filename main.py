from culture_poly import culture_poly

willStop = False
size = get_world_size()
rows = size
cols = size

while willStop == False:
	willStop = culture_poly(rows, cols, 7, 7, 16, 16, 7, 7, 0)