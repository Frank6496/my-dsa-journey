name = input("Enter your full name: ")
age = int(input("Please enter your age: "))

preg_dur = int(input("How old is your pregnancy: "))

print(f"Hello {name} you are {age} years old, and your pregancy is {preg_dur} months old")


num1 = int(input("Enter any number : "))
num2 = int(input("Enter any number : "))

choice = input("What do you want to do e.g Add, Substract, Multiply, Divide : ")


if choice == "Addition":
    print(num1 + num2)
elif choice == "Substract":
    print(num1 - num2)
elif choice == "Multiply":
    print(num1 * num2)
elif choice == "Division":
    print(num1 / num2)
else:
    print("No operation can be done")
