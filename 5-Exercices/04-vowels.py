text = input("Insert a sentence or a word: ")

vowels = {'a', 'e', 'i', 'o', 'u'}

text = text.lower()

result = len([word for word in text if word in vowels])
print(f"The result it's {result}")