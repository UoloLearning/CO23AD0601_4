ballACoord = 10.9
ballBCoord = 100.8
ballA_mass = 2
ballBMass = 3
distance = ballBCoord - ballACoord
valueOfG = 0.00000000006674
__force = (valueOfG * ballA_mass * ballBMass) / (distance * distance)
print(__force)
