#Project with max, min, reverse, sorted, filter

print("Hi welcome to number sorter powered by Python")
print("It can do the following:\n 1.find the biggest and smallest numbers in a numbers set\n 2.can sort them from smallest to biggest or the opposite\n 3. can also print all the even or odd numbers in your muber set ")

#numbers for the number set
numbers= []

numberInput= int(input("Enter Number: "))
numbers.append(numberInput)

while numberInput != 000:
    numberInput= int(input("Enter Number: "))
    numbers.append(numberInput)
    
 
numbers.remove(0)
print(numbers)


task= input("Are you ready to do something with this set? Type anything to continue\n ")

print("These are the commands that can be given: ")
print("1. find max - to find biggest value in set")
print("2. find min - to find smallest value in set")
print("3. reverse set - to reverse order of set")
print("4. sort small to large - to sort values from smallest to largest")
print("5. sort large to small - to sort values from largest to smallest")
print("6. find even numbers - to print all even numbers in set")
print("7. find odd numbers - to print all odd numbers in set")
print("8. done - to end")


while task != "done":
    task= input("What would you like to do with this set?")

    if task == "find max":
        print(max(numbers))
    elif task == "find min":
        print(min(numbers))
    elif task == "reverse set":
        print(list(reversed(numbers)))
    elif task == "sort small to large":
        print(sorted(numbers))
    elif task == "sort large to small":
        numbers.sort(reverse =True)
        print(numbers)
    elif task == "find even numbers":
        evens = filter(lambda num: num % 2 == 0, numbers)
        print(list(evens))
    elif task == "find odd numbers":
        odds= filter(lambda num: num % 2 != 0, numbers)
        print(list(odds))
    else:
        print("enter an actual task")


print("Bye")





