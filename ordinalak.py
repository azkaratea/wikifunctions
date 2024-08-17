def Z18742(Z18742K1):
	if (Z18742K1 == "bat"):
		emaitza = "lehenengo"
	elif (Z18742K1.endswith("bost")):
		emaitza = Z18742K1[:-1]
		emaitza = emaitza + "garren"
	elif (Z18742K1.endswith("oi bat")):
		emaitza = Z18742K1[:-4]
		emaitza = emaitza + "garren"
	else:
		emaitza = Z18742K1 + "garren"
	
	return emaitza
