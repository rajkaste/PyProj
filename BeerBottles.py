numberOfBottles = 10
while (numberOfBottles > 0): 
    bottleWord = "bottles"
    if (numberOfBottles == 1):
        bottleWord = "bottle"
    print(numberOfBottles,bottleWord,"of beer on the wall")
    print(numberOfBottles,bottleWord,"of beer,")
    print("Take one down, pass it around,")
    numberOfBottles = numberOfBottles - 1
print("Buy new bottles...!")
