# WAP to accept comma separated numbers from user
# and generate a list and tuple

numbers = input("Input some numbers separated by commas: ")

list1 = numbers.split(",")
tuple1 = tuple(list1)

print("List - ",list1)
print("Tuple - ",tuple1)
