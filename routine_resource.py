def routine_get_carrot_seed(minQuantity=4, buyAmount=4):
	if num_items(Items.Carrot_Seed) <= minQuantity:
		if num_items(Items.Wood) >= buyAmount and num_items(Items.Hay) >= buyAmount:
			trade(Items.Carrot_Seed, buyAmount)
		else:
			pass

def routine_get_pumpkin_seed(minQuantity=4, buyAmount=4):
	if num_items(Items.Pumpkin_Seed) <= minQuantity:
		if num_items(Items.Carrot) >= buyAmount:
			trade(Items.Pumpkin_Seed, buyAmount)
		else:
			pass

def routine_get_sunflower(minQuantity=4, buyAmount=4):
	if num_items(Items.Sunflower_Seed) <= minQuantity:
		trade(Items.Sunflower_Seed, buyAmount)

def routine_get_tank(minQuantity=100, buyAmount=5):
		if num_items(Items.Empty_Tank) <= minQuantity:
			trade(Items.Empty_Tank, buyAmount)
		else:
			pass
