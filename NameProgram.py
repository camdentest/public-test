# Sample Program

name = input("Hi! What is your name? ")
print("\nHello " + name + "!")

firstLetter = name[0].capitalize()

if firstLetter >= "A" and firstLetter <= "H":
	print("Your name is at the beginning of the alphabet")
elif firstLetter >= "I" and firstLetter <= "R":
	print("Your name is in the middle of the alphabet")
elif firstLetter >= "S" and firstLetter <= "Z":
	print("Your name is at the end of the alphabet")
else:
	print("The first letter of your name isn't in the alphabet")