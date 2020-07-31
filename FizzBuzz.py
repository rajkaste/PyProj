def fizzBuzz():
    output = []
    count = 1
    while(count <= 100): 
        if (count % 3 == 0 and count % 5 == 0):
            output.append("FizzBuzz")
        elif (count % 5 == 0):
            output.append("Buzz")
        elif (count % 3 == 0):
            output.append("Fizz")
        else:
            output.append(count)
        count = count + 1
    print(output)

fizzBuzz()