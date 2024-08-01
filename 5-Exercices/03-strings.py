output = ""

while True:
    if not output:
        text = input("Insert a word or sentence or exit to leave: ")
        if text.lower() == "exit":
            break

    print(f"The result it's {text[::-1]}")
    