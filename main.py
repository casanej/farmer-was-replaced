from culture_poly import culture_poly

willStop = False

while willStop == False:
	rows = 8
	cols = 8
	willStop = culture_poly(rows, cols, 7, 7, 16, 16, 7, 7, 0)