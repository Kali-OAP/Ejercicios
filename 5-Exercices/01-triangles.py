b = ""
h = ""
while True:
    if not b:
        base = input("Insert a base of the triangle: ")
        if base.lower() == "exit":
            break
    
    try:
        b = int(base)
    except ValueError:
        print("Insert a number")
        continue
    high = input("Insert a high for the triangle: ")
    if high.lower() == "exit":
        break
    try:
        h = int(high)
    except ValueError:
        print("Insert a number")
        continue

    
    print(f"The result of the base of triangle {base} and {high} it's {b * h / 2}")
    break