
list_numbers = input("Insert a list of numbers, please use commas (,) to split: ")

output = [int(number) for number in list_numbers.split(",")]

result = [number for number in output if number > 5]

print(result)