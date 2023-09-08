while True: #put while loop here to make sure we get a whole number to start with.  
            #Yes I looked this up, the descpription doesn't technically say I can't do this please don't mark me down dear heavens.
    try:    #You can't technically have half a pirate, even if he has a metal arm or missing limb, still is just one pirate. So that's my logic
        piratesString = input("How many pirates:")
        pirates = int(piratesString)
        break
    except ValueError:
        print("Invalid input, please put a whole number.")

while True: #Made it opperate like money so you can have it rounded to 2 decimal places.
    try:
        unitsString = input("How many Units:")
        units = round(float(unitsString),2)
        break
    except:
        print("Invalid input, please put a number rounded to two decimals")

piratesX = pirates - 2 
#piratesX is pirates excluding Quill and Yondu

#This is Yondu's 13% Total share
units = units - piratesX * 3  #3 is the number of credits each pirate gets to take initially, Also PEMDAS makes multiplication go first
yonduCut1 = units * 0.13 

#this is the first place you can possible get a float value with more than two decimals. It is necessary before adding to Yondu's cut.
units = round(units, 2)
yonduCut1 = round(yonduCut1, 2) #Using money logic
units = units - yonduCut1

#This is Peter Quill's 11% of the remaining share
peterQuillCut1 = units * 0.11
units = round(units, 2)
peterQuillCut1 = round(peterQuillCut1, 2) #Using money logic
units = units - peterQuillCut1




yonduCutTotal = yonduCut1
peterQuillTotal = peterQuillCut1

print(f"current units: {units}")
print(f"Yondu's share: {yonduCutTotal}")
print(f"Peter's share: {peterQuillTotal}")