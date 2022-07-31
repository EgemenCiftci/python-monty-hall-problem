import random

def getRandomDoor(doors):
    return random.choice(doors)

def getRandomDoorExcept(doors, prizeDoor, selectedDoor):
    return random.choice(list(filter(lambda f : (f != prizeDoor and f != selectedDoor), doors)))

def calculateChance(isSwitchDoor):
    doors = [0,1,2]
    sampleCount = 100000
    a = 0
    for i in range(sampleCount):
        prizeDoor = getRandomDoor(doors)
        selectedDoor = getRandomDoor(doors)
        emptyDoor = getRandomDoorExcept(doors, prizeDoor, selectedDoor)

        if isSwitchDoor:
            selectedDoor = getRandomDoorExcept(doors, selectedDoor, emptyDoor)
        
        isWin = prizeDoor == selectedDoor
        if isWin:
            a += 1
    return a * 100 / sampleCount

print("Win Chance (Stay): " + str(calculateChance(False)) + "%")
print("Win Chance (Switch): " + str(calculateChance(True)) + "%")