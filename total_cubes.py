def sol(sides, painted):
	if sides == 1:
		if painted == 4:
			return 1
		else: return 0 
	if painted == 1:
		no_of_cubes = ((sides - 2) ** 2) * 6
	if painted == 2:
		no_of_cubes = ((sides - 2) * 3) * 4 
	if painted == 3:
		no_of_cubes = 8
	if painted == 4:
		no_of_cubes = 0
	return no_of_cubes

