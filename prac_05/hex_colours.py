COLOUR_TO_HEX = {"aliceblue": "#f0f8ff", "aqua": "#00ffff", "black": "#000000", "blue": "#0000ff", "eggshell": "#f0ead6",
                "hotpink": "#ff69b4", "indigo": "#4b0082", "pink": "#ffc0cb", "red": "	#ff0000", "yellow": "#ffff00"}
print(COLOUR_TO_HEX)

colour = input("please enter a colour on the list: ").lower()
while colour != "":
    try:
        print(colour, "is", COLOUR_TO_HEX[colour])
    except KeyError:
        print("Colour is not on the list")
    colour = input("please enter a colour on the list: ").lower()
print("Good Bye")