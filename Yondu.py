piratesString = input("How many pirates:")
pirates = int(piratesString)

unitsString = input("How many Units:")
units = int(unitsString)

piratesX = pirates - 2
units = units - piratesX * 3
yonduCut1 = units * 0.13
round(units, 2)
units = units - yonduCut1



yonduCutTotal = yonduCut1

print(f"current units: {units}")
print(f"Yondu's share: {yonduCutTotal}")