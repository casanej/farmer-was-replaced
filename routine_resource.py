def routine_get_carrot_seed(minQuantity=4, buyAmount=4):
	tradeCost = 12
	totalCost = tradeCost * buyAmount

	if num_items(Items.Wood) >= totalCost and num_items(Items.Hay) >= totalCost:
		if num_items(Items.Carrot_Seed) <= minQuantity:
			trade(Items.Carrot_Seed, buyAmount)
	else:
		quick_print("ERROR: Not enough wood and / or hay to trade for carrot seeds")

def routine_get_cactus_seed(minQuantity=4, buyAmount=4):
	tradeCost = 40
	totalCost = tradeCost * buyAmount
	if num_items(Items.Gold) >= totalCost:
		if num_items(Items.Cactus_Seed) <= minQuantity:
			trade(Items.Cactus_Seed, buyAmount)
	else:
		quick_print("ERROR: Not enough gold to trade for cactus seeds")

def routine_get_pumpkin_seed(minQuantity=4, buyAmount=4):
	tradeCost = 10
	totalCost = tradeCost * buyAmount
	if num_items(Items.Carrot) >= totalCost:
		if num_items(Items.Pumpkin_Seed) <= minQuantity:
			trade(Items.Pumpkin_Seed, buyAmount)
	else:
		quick_print("ERROR: Not enough pumpkin seeds to trade for carrots")

def routine_get_sunflower(minQuantity=4, buyAmount=4):
	tradeCost = 6
	totalCost = tradeCost * buyAmount
	if num_items(Items.Carrot) >= totalCost:
		if num_items(Items.Sunflower_Seed) <= minQuantity:
			trade(Items.Sunflower_Seed, buyAmount)
	else:
		quick_print("ERROR: Not enough carrots to trade for sunflowers seeds")

def routine_get_tank(minQuantity=100, buyAmount=5):
	if num_items(Items.Water_Tank) >= minQuantity:
		if num_items(Items.Empty_Tank) <= minQuantity:
			trade(Items.Empty_Tank, buyAmount)

def routine_get_eggs(minQuantity=100, buyAmount=5):
	tradeCost = 60
	totalCost = tradeCost * buyAmount
	if num_items(Items.Pumpkin_Seed) >= totalCost:
		if num_items(Items.Egg) <= minQuantity:
			trade(Items.Egg, buyAmount)
	else:
		quick_print("ERROR: Not enough Cactus to trade for eggs")

def routine_get_fertilizer(minQuantity=100, buyAmount=5):
	tradeCost = 10
	totalCost = tradeCost * buyAmount
	if (num_items(Items.Pumpkin) >= totalCost):
		if num_items(Items.Fertilizer) <= minQuantity:
			trade(Items.Fertilizer, buyAmount)
	else:
		quick_print("ERROR: Not enough pumpkins to trade for fertilizer")