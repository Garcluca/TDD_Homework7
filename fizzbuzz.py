def code():
    #i = 1
    result = ""
    for i in range(101):
        if i == 0 :
            continue
        if i % 15==0 and i !=0:
            result+="Fizzbuzz"
            print("FizzBuzz")
        elif i % 3==0:
            result+= "Fizz"
            print("Fizz")
        elif i % 5==0:
            result+= "Buzz"
            print("Buzz")
        else:
            result+= str(i)
            print(i)
    print(result)
    return result 
