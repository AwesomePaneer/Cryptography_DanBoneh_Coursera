alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

stringInput = input("Enter a string: ")
length = len(stringInput)
stringOutput = ""

shift = int(input("Enter the shift: "))

for i in range(length):
    character = stringInput[i]
    loc = alpha.find(character.upper())
    stringOutput += alpha[(loc+shift)%26]

print("Encrypted text is ", stringOutput)
